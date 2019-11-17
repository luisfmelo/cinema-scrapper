package models

import (
	"errors"
	"github.com/jinzhu/gorm"
)

type Movie struct {
	gorm.Model

	Title     string   `json:"title" gorm:"unique,not null"`
	Year      int      `json:"year"`
	AgeRating string   `json:"age_rating"`
	Duration  int      `json:"duration"`
	Genre     string   `json:"genre"`
	Country   string   `json:"country"`
	Version   *string  `json:"version"`
	Format    *string  `json:"format"`
	Synopsis  *string  `json:"synopsis"`
	Trailer   *string  `json:"trailer"`
	ImdbURL   *string  `json:"imdb_url"`
	Rating    *float64 `json:"rating"`
	Poster    *string  `json:"poster"`
}

func SaveMovie(movie *Movie) error {
	db := db.Where(Movie{Title: movie.Title}).FirstOrCreate(&movie)
	if db.Error != nil {
		return errors.New("failed to create a cinema. " + db.Error.Error())
	}

	if movie.ID <= 0 {
		return errors.New("failed to create a cinema, connection error")
	}

	return nil
}
