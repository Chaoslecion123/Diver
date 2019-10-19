<template>
  <BaseAuthView>
    <d-password-reset-form/>
  </BaseAuthView>
</template>

<script>
import BaseAuthView from './Base.vue'
import Password from './d-password'

export default {
  name: 'PasswordReset',
  components: {
    'BaseAuthView': BaseAuthView,
    'd-password-reset-form': Password.ResetForm
  }
}
</script>
