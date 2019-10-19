<template>
  <BaseAuthView>
    <d-login-form/>
  </BaseAuthView>
</template>

<script>
import BaseAuthView from './Base.vue'
import LogIn from './d-login'

export default {
  name: 'LogIn',
  components: {
    'BaseAuthView': BaseAuthView,
    'd-login-form': LogIn.Form
  }
}
</script>
