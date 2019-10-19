<template>
  <BaseAuthView>
    <d-signup-form/>
  </BaseAuthView>
</template>

<script>
import BaseAuthView from './Base.vue'
import SignUp from './d-signup'

export default {
  name: 'SignUp',
  components: {
    'BaseAuthView': BaseAuthView,
    'd-signup-form': SignUp.Form
  }
}
</script>
