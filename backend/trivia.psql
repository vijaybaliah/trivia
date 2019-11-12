--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5
-- Dumped by pg_dump version 11.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: vijay
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO vijay;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: vijay
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    type character varying
);


ALTER TABLE public.categories OWNER TO vijay;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: vijay
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_id_seq OWNER TO vijay;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vijay
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: questions; Type: TABLE; Schema: public; Owner: vijay
--

CREATE TABLE public.questions (
    id integer NOT NULL,
    question character varying,
    answer character varying,
    difficulty integer,
    category_id integer NOT NULL
);


ALTER TABLE public.questions OWNER TO vijay;

--
-- Name: questions_id_seq; Type: SEQUENCE; Schema: public; Owner: vijay
--

CREATE SEQUENCE public.questions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.questions_id_seq OWNER TO vijay;

--
-- Name: questions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vijay
--

ALTER SEQUENCE public.questions_id_seq OWNED BY public.questions.id;


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: vijay
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: questions id; Type: DEFAULT; Schema: public; Owner: vijay
--

ALTER TABLE ONLY public.questions ALTER COLUMN id SET DEFAULT nextval('public.questions_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: vijay
--

COPY public.alembic_version (version_num) FROM stdin;
53366d9c87cf
\.


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: vijay
--

COPY public.categories (id, type) FROM stdin;
1	Science
2	Art
3	Geography
4	History
5	Entertainment
6	Sports
\.


--
-- Data for Name: questions; Type: TABLE DATA; Schema: public; Owner: vijay
--

COPY public.questions (id, question, answer, difficulty, category_id) FROM stdin;
1	Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?	Maya Angelou	2	4
2	What boxer's original name is Cassius Clay?	Muhammad Ali	1	4
3	What movie earned Tom Hanks his third straight Oscar nomination, in 1996?	Apollo 13	4	5
4	What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?	Tom Cruise	4	5
5	What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?	Edward Scissorhands	3	5
6	Which is the only team to play in every soccer World Cup tournament?	Brazil	3	6
7	Which country won the first ever soccer World Cup in 1930?	Uruguay	4	6
8	Who invented Peanut Butter?	George Washington Carver	2	4
9	What is the largest lake in Africa?	Lake Victoria	2	3
10	In which royal palace would you find the Hall of Mirrors?	The Palace of Versailles	3	3
11	The Taj Mahal is located in which Indian city?	Agra	2	3
12	Which Dutch graphic artist–initials M C was a creator of optical illusions?	Escher	1	2
13	La Giaconda is better known as what?	Mona Lisa	3	2
14	How many paintings did Van Gogh sell in his lifetime?	One	4	2
15	Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?	Jackson Pollock	2	2
16	What is the heaviest organ in the human body?	The Liver	4	1
17	Who discovered penicillin?	Alexander Fleming	3	1
18	Hematology is a branch of medicine involving the study of what?	Blood	4	1
19	Which dung beetle was worshipped by the ancient Egyptians?	Scarab	4	4
\.


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vijay
--

SELECT pg_catalog.setval('public.categories_id_seq', 6, true);


--
-- Name: questions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vijay
--

SELECT pg_catalog.setval('public.questions_id_seq', 19, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: vijay
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: categories pk_categories; Type: CONSTRAINT; Schema: public; Owner: vijay
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT pk_categories PRIMARY KEY (id);


--
-- Name: questions pk_questions; Type: CONSTRAINT; Schema: public; Owner: vijay
--

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT pk_questions PRIMARY KEY (id);


--
-- Name: questions fk_questions_category_id_categories; Type: FK CONSTRAINT; Schema: public; Owner: vijay
--

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT fk_questions_category_id_categories FOREIGN KEY (category_id) REFERENCES public.categories(id);


--
-- PostgreSQL database dump complete
--

