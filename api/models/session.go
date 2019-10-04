package models

import (
	"github.com/jinzhu/gorm"
	"time"
)

type Session struct {
	gorm.Model

	ID        uint64 `gorm:"primary_key"`
	CreatedAt time.Time
	UpdatedAt time.Time
	DeletedAt *time.Time
	Name      string `sql:"type:varchar(30)"`
}