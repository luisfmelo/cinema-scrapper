package models

import (
	"errors"
	"github.com/jinzhu/gorm"
)

type Cinema struct {
	gorm.Model

	Name      string   `json:"name"`
	City      string   `json:"city"`
	Company   string   `json:"company"`
	Latitude  *float64 `json:"latitude"`
	Longitude *float64 `json:"longitude"`
}

func SaveCinema(cinema *Cinema) error {
	c := db.Where(Cinema{Name: cinema.Name, City: cinema.City, Company: cinema.Company}).
		FirstOrCreate(&cinema)

	if c.Error != nil {
		return errors.New("failed to create a cinema. " + c.Error.Error())
	}
	if cinema.ID <= 0 {
		return errors.New("failed to create a cinema, connection error")
	}

	return nil
}
