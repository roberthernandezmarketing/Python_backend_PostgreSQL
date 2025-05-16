SELECT * FROM authors;

SELECT * FROM posts;

SELECT * FROM tags;

SELECT * FROM post_tags;

INSERT INTO tags (name) 
  VALUES ('Test3');

SELECT MAX(id) FROM tags;
SELECT nextval('tags_id_seq');
SELECT setval ('tags_id_seq');

TRUNCATE TABLE tags RESTART IDENTITY CASCADE;
