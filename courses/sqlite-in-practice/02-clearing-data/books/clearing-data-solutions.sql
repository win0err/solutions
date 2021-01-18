create table books(book_id integer, title text, authors text, average_rating real, isbn text, isbn13 text, language_code text, num_pages integer, ratings_count integer, text_reviews_count integer, publication_date text, publisher text);

.import --csv --skip 1 books.csv books

select book_id, ratings_count from books order by 2 desc limit 1;

select book_id, ratings_count, average_rating from books where ratings_count > 100 order by average_rating desc limit 1;

select round(avg(average_rating), 2) from books where ratings_count > 100;

update books set language_code = 'eng' where language_code like 'en%';

select language_code, count(*) from books group by language_code;

alter table books add column author TEXT;

update books set author = case when instr(authors, '/') > 0 then substr(authors, 0, instr(authors, '/')) else authors end;

select count(*) as books_count, author from books group by author order by 1 desc limit 5;
