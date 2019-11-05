package controllers

import (
	"cinema-scrapper/api/models"
	"cinema-scrapper/api/requests"
	"cinema-scrapper/api/responses"
	"net/http"
)

func CreateCinema(w http.ResponseWriter, r *http.Request) {

	cinema := models.Cinema{}
	err := requests.ParseRequest(r, &cinema)
	if err != nil {
		responses.ERROR(w, http.StatusUnprocessableEntity, err)
		return
	}

	err = models.SaveCinema(&cinema)
	if err != nil {
		responses.ERROR(w, http.StatusBadRequest, err)
		return
	}

	responses.JSON(w, http.StatusCreated, cinema)
}
