package controllers

import (
	"cinema-scrapper/api/models"
	"cinema-scrapper/api/requests"
	"cinema-scrapper/api/responses"
	"net/http"
)

func CreateMovie(w http.ResponseWriter, r *http.Request) {
	movie := models.Movie{}
	err := requests.ParseRequest(r, &movie)
	if err != nil {
		responses.ERROR(w, http.StatusUnprocessableEntity, err)
		return
	}

	err = models.SaveMovie(&movie)
	if err != nil {
		responses.ERROR(w, http.StatusBadRequest, err)
		return
	}

	responses.JSON(w, http.StatusCreated, movie)
}
