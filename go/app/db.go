package main

import (
	"database/sql"
	"os"

	_ "github.com/mattn/go-sqlite3"
)

func loadDb(path string) (*sql.DB, error) {
	// Open database
	db, err := sql.Open("sqlite3", path)
	if err != nil {
		return nil, err
	}
	if err := createTableIfNotExists(db); err != nil {
		return nil, err
	}
	return db, nil
}

func createTableIfNotExists(db *sql.DB) error {
	// Create table if not exists
	bytes, err := os.ReadFile(DbSchemaPath)
	if err != nil {
		return err
	}
	schema := string(bytes)
	_, err = db.Exec(schema) // CREATE TABLE IF NOT EXIST ...;
	return err
}

func scanItem(rows *sql.Rows) (*Item, error) {
	var item Item
	if err := rows.Scan(&item.Id, &item.Name, &item.CategoryId, &item.ImageName); err != nil {
		return nil, err
	}
	return &item, nil
}

func scanCategory(rows *sql.Rows) (*Category, error) {
	var category Category
	if err := rows.Scan(&category.Id, &category.Name); err != nil {
		return nil, err
	}
	return &category, nil
}

func scanResponseItem(rows *sql.Rows) (*ResponseItem, error) {
	var response_item ResponseItem
	if err := rows.Scan(&response_item.Id, &response_item.Name, &response_item.Category, &response_item.Image_name); err != nil {
		return nil, err
	}
	return &response_item, nil
}

func scanResponseItems(rows *sql.Rows) (*ResponseItems, error) {
	var response_items ResponseItems
	for rows.Next() {
		response_item, err := scanResponseItem(rows)
		if err != nil {
			return nil, err
		}
		response_items.Items = append(response_items.Items, *response_item)
	}
	return &response_items, nil
}

func loadItemById(db *sql.DB, id int) (*Item, error) {
	// Load item from db by id
	rows, err := db.Query("SELECT * FROM items WHERE items.id = ?", id)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	if !rows.Next() {
		return nil, nil
	}
	return scanItem(rows)
}

func loadCategoryById(db *sql.DB, id int) (*Category, error) {
	// Load category from db by id
	rows, err := db.Query("SELECT * FROM categories WHERE categories.id = ?", id)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	if !rows.Next() {
		return nil, nil
	}
	return scanCategory(rows)
}

func insertItem(db *sql.DB, name string, category_id int, image_name string) error {
	// Save new items to database
	_, err := db.Exec("INSERT INTO items (name, category_id, image_name) VALUES (?, ?, ?)", name, category_id, image_name)
	return err
}

func insertCategory(db *sql.DB, category_name string) error {
	// Save new category to database
	_, err := db.Exec("INSERT INTO categories (name) VALUES (?)", category_name)
	return err
}

func loadResponseItemsByKeyword(db *sql.DB, keyword string) (*ResponseItems, error) {
	query := JoinAllQuery + " AND items.name LIKE CONCAT('%', ?, '%')"
	rows, err := db.Query(query, keyword)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	return scanResponseItems(rows)
}

func loadCategoryByName(db *sql.DB, category_name string) (*Category, error) {
	rows, err := db.Query("SELECT * FROM categories WHERE categories.name = ?", category_name)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	if !rows.Next() {
		return nil, nil
	}
	return scanCategory(rows)
}

func joinItemAndCategory(db *sql.DB, item Item) (*ResponseItem, error) {
	category, err := loadCategoryById(db, item.CategoryId)
	if err != nil {
		return nil, err
	}
	if category == nil {
		return nil, nil
	}

	response_item := ResponseItem{Id: item.Id, Name: item.Name, Category: category.Name, Image_name: item.ImageName}
	return &response_item, nil
}

func joinAll(db *sql.DB) (*ResponseItems, error) {
	// Join category name to items
	rows, err := db.Query(JoinAllQuery)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	return scanResponseItems(rows)
}
