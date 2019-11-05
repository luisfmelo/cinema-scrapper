<template>
  <div>
  </div>
</template>

<script>

export default {
  props: ['movie'],
  data() {
    return {
      cart: [], // this.$store.state.cart,
    };
  },
  computed: {
    isAdding() {
      return true; // this.cart.indexOf(this.movie) < 0;
    },
  },
  methods: {
    /* addToCart() {
      this.$store.commit(ADD_TO_CART, this.movie);
    },
    removeFromCart(id) {
      this.$store.commit(REMOVE_FROM_CART, id);
    }, */
  },
};
</script>
