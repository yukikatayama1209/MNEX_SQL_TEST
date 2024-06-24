CREATE TABLE hobbys (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    product VARCHAR(255) NOT NULL,
    purchase_date DATE NOT NULL,
    shop_location VARCHAR(255) NOT NULL,
    hobby_photo TEXT NOT NULL,
    comments TEXT,
    good INT
);
