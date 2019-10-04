package models

import (
	"github.com/jinzhu/gorm"
	"time"
)

type Movie struct {
	gorm.Model

	ID            uint64 `gorm:"primary_key"`
	CreatedAt     time.Time
	UpdatedAt     time.Time
	DeletedAt     *time.Time
	Title         string `sql:"type:varchar(128)"`
	OriginalTitle string `sql:"type:varchar(128)"`
	Year          string `sql:"type:integer"`
	AgeRating     string `sql:"type:varchar(64)"`
	Duration      string `sql:"type:integer"`
	Genre         string `sql:"type:varchar(128)"`
	Country       string `sql:"type:varchar(128)"`
	Synopsis      string `sql:"type:varchar(128)"`
	Trailer       string `sql:"type:varchar(128)"`
}