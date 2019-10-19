<template>
  <BaseAuthView>
    <d-password-recovery-form/>
  </BaseAuthView>
</template>

<script>
import BaseAuthView from './Base.vue'
import Password from './d-password'

export default {
  name: 'PasswordRecovery',
  components: {
    'BaseAuthView': BaseAuthView,
    'd-password-recovery-form': Password.RecoveryForm
  }
}
</script>
