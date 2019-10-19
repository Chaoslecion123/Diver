/* global Culqi */
(function ($) {
  function waitFotPayment () {
    $('body').waitMe({
      effect: 'orbit',
      text: 'Procesando pago...',
      bg: 'rgba(255,255,255,0.7)',
      color: '#28d2c8'
    });
  }

  function setupCulqi () {
    var data = document.getElementById('id_culqi').dataset;

    /**
     * Setup Culqi object
     */
    Culqi.publicKey = data.key;
    Culqi.settings({
      title: data.name,
      currency: data.currency,
      description: data.description,
      amount: data.amount
    });
  }

  function culqi () {
    var paymentForm = document.getElementById('payment-form');

    if (Culqi.token) {
      var paymentIdField = document.getElementById('id_culqi_payment_id');
      paymentIdField.value = Culqi.token.id;
    }

    paymentForm.submit();
    waitFotPayment();
  };

  var paymentForm = document.getElementById('payment-form');
  var submitButton = document.createElement('input');

  submitButton.type = 'submit';
  submitButton.value = 'Pay now with Culqi';
  submitButton.classList.add('culqi-payment-button');
  submitButton.addEventListener('click', function (e) {
    setupCulqi();
    Culqi.open();
    e.preventDefault();
  }, false);

  paymentForm.appendChild(submitButton);
  window.culqi = culqi;
})(jQuery);
