package controllers

import (
	"cinema-scrapper/api/models"
	"cinema-scrapper/api/requests"
	"cinema-scrapper/api/responses"
	"net/http"
)

func CreateSession(w http.ResponseWriter, r *http.Request) {

	session := models.Session{}
	err := requests.ParseRequest(r, &session)
	if err != nil {
		responses.ERROR(w, http.StatusUnprocessableEntity, err)
		return
	}

	err = models.SaveSession(&session)
	if err != nil {
		responses.ERROR(w, http.StatusBadRequest, err)
		return
	}

	responses.JSON(w, http.StatusCreated, session)
}
