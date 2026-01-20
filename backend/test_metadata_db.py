from metadata_db import init_db, insert_item, get_item

def test_metadata_db():
    init_db()

    test_id = "test-123"
    image_path = "uploads/test_image.jpg"
    contact_number = "9999999999"

    insert_item(test_id, image_path, contact_number)

    item = get_item(test_id)
    print(item)

if __name__ == "__main__":
    test_metadata_db()
