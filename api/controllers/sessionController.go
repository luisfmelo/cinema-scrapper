package controllers

import (
	"cinema-scrapper/api/models"
	u "cinema-scrapper/api/utils"
	"encoding/json"
	"net/http"
)

var CreateSession = func(w http.ResponseWriter, r *http.Request) {

	session := &models.Session{}

	err := json.NewDecoder(r.Body).Decode(session)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}

	resp := session.Create()
	u.Respond(w, resp)
}