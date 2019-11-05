<template>
  <div>
    <div class="movies">
      <div class="container">
       <!--<template v-for="movie in movies">
          <movie-item :movie="movie"></movie-item>
        </template>-->
      </div>
    </div>
  </div>
</template>

<script>
import MovieItem from './MovieItem';

export default {
  name: 'movie-list',
  created() {
    if (this.movies.length === 0) {
      this.$store.dispatch('allMovies');
    }
  },
  computed: {
    movies() {
      return this.$store.getters.allMovies;
    },
  },
  data() {
    return {};
  },
  components: {
    'movie-item': MovieItem,
  },
};
</script>

<style>
  .movies {
    background: #F7F8FB;
    padding: 30px 0;
  }
</style>
