show databases;
use facebook;
use ptt;
use youtube;
use mobile01;

show tables;
desc facebook_shumai_momo_bert;
desc facebook_shumai_pchome_bert;
SELECT id, source, keyword, time, comment, score FROM facebook_shumai_momo_bert;
SELECT id, source, keyword, time, comment, score FROM facebook_shumai_pchome_bert;


desc momo;
desc pchome;
desc shopee;

SELECT id, source, keyword, time, comment, score FROM momo;
SELECT id, source, keyword, time, comment, score FROM pchome;
SELECT id, source, keyword, time, comment, score FROM shopee;

-- 改CSV 和 .py 比較快
-- SELECT source, keyword, time, comment, CAST(SUBSTRING_INDEX(score, ':', -1) AS FLOAT) AS score FROM momo;
-- SELECT source, keyword, time, comment, CAST(SUBSTRING_INDEX(score, ':', -1) AS FLOAT) AS score FROM pchome;
-- SELECT source, keyword, time, comment, CAST(SUBSTRING_INDEX(score, ':', -1) AS FLOAT) AS score FROM shopee;



desc youtube_data;
ALTER TABLE youtube_data MODIFY COLUMN comment varchar(2000);
ALTER TABLE youtube_data MODIFY COLUMN score float;
SELECT id, source, keyword, time, comment, score FROM youtube_data WHERE comment Like "%Momo%" or "momo" or "%MOMO%";
SELECT id, source, keyword, time, comment, score FROM youtube_data WHERE comment Like "%Pchome%" or "PCHOME" or "%Pchome%";
SELECT id, source, keyword, time, comment, score FROM youtube_data WHERE comment Like "%Shopee%" or "shopee" or "%蝦皮%";


desc mobile01_bert;
ALTER TABLE mobile01_bert ADD COLUMN id int primary key auto_increment;
ALTER TABLE mobile01_bert MODIFY COLUMN time date;
select * from mobile01_bert;
select id, source, keyword, time, comment, score FROM mobile01_bert WHERE keyword Like "momo";
select id, source, keyword, time, comment, score FROM mobile01_bert WHERE keyword Like "pchome";
select id, source, keyword, time, comment, score FROM mobile01_bert WHERE keyword Like "蝦皮";


ALTER TABLE mobile01_bert CHANGE predict score float;
ALTER TABLE mobile01_bert MODIFY COLUMN predict FLOAT;

