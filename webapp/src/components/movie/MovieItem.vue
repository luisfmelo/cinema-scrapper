<template>
  <div class="col-lg-3 col-md-4 col-sm-6 col-xs-12">
    <div class="movie">
      <router-link :to="'/details/'+movie._id" class="movie-link">
        <div class="movie__image">
          <img
            class="img-responsive" :src="movie.image" alt="">
        </div>
        <div class="movie__description">
          <div class="movie__info">
            <small>{{movie.manufacturer.name}}</small>
            <h4>{{movie.name}}</h4>
          </div>
          <div class="movie__price-cart">
            ${{movie.price}}
          </div>
        </div>
      </router-link>
      <!--<div class="movie__action">
        <movie-button :movie="movie"></movie-button>
        <button class="button"><i class="fa fa-cart-plus"></i> Add to Cart</button>
      </div>-->
    </div>
  </div>
</template>

<script>
export default {
  name: 'movie-item',
  props: ['movie'],
};
</script>

<style>
  .movie {
    background: #FFF;
    margin-bottom: 30px;
    position: relative;
    overflow: hidden;
  }
  .movie .movie__description,
  .movie .movie__action {
    transition: 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275) transform;
  }
  .movie:hover .movie__description {
    transform: translateY(-40px);
  }
  .movie:hover .movie__action {
    transform: none;
  }
  .movie-link {
    display: block;
    color: #3D3D3D;
  }
  .movie-link:hover {
    color: #3D3D3D;
    text-decoration: none;
  }
  .movie .movie__image {
    width: 100%;
  }
  .movie__image img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    height: 225px;
  }
  .movie__description {
    width: 100%;
    display: flex;
    padding: 20px 20px 15px;
    background: #FFF;
  }
  .movie__info {
    flex: 2;
  }
  .movie__description small {
    color: #808080;
  }
  .movie__description h4 {
    margin: 3px 0 5px 0;
  }
  .movie__price-cart {
    flex: 1;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    font-size: 20px;
    font-weight: bold;
    color: #51D2B7;
  }
  .movie__price-cart p {
    flex-grow: 2;
    font-size: 20px;
    font-weight: bold;
  }
  .movie__action {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    transform: translateY(100%);
  }
  .movie__action button {
    border-radius: 0;
    width: 100%;
    display: block;
  }
</style>
