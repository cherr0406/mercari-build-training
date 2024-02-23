package main

const (
	ImgDir       = "images"
	ItemsJson    = "items.json"
	DbPath       = "../db/mercari.sqlite3"
	DbSchemaPath = "../db/items.db"
)

const (
	ItemsTableName      = "items"
	CategoriesTableName = "categories"
	JoinAllQuery        = "SELECT items.id, items.name, categories.name, items.image_name FROM items INNER JOIN categories ON items.category_id = categories.id"
)

type Response struct {
	Message string `json:"message"`
}

type Items struct {
	Items []Item `db:"items"`
}

type Item struct {
	Id         int    `db:"id"`
	Name       string `db:"name"`
	CategoryId int    `db:"category_id"`
	ImageName  string `db:"image_name"`
}

type Categories struct {
	Categories []Category `db:"categories"`
}

type Category struct {
	Id   int    `db:"id"`
	Name string `db:"name"`
}

type ResponseItems struct {
	Items []ResponseItem `json:"items"`
}

type ResponseItem struct {
	Id         int    `json:"id"`
	Name       string `json:"name"`
	Category   string `json:"category"`
	Image_name string `json:"image_name"`
}
