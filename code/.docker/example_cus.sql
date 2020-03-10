--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.15
-- Dumped by pg_dump version 9.6.16

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

--
-- Data for Name: bsu_eformsschemadetail; Type: TABLE DATA; Schema: public
--

INSERT INTO public.bsu_clientlist VALUES ('BobCU','Bob''s Credit Union',
    '1 S. Capitol','','Boise','Idaho',
    '55555','bob@bob.bob','555-555-5555',
    'Bob Bobberson','Bob!');
INSERT INTO public.bsu_clientlist VALUES ('SoundCU','Sound Credit Union',
    '2 1st street','','Seattle','Washington',
    '55255','contact@soundcu.example','555-555-2837',
    'Alice Doe','');
INSERT INTO public.bsu_clientlist VALUES ('ExampleCU','Example Credit Union',
    '163 George St.','Suite 101','Buffalo','New York',
    '55325','contact@example.com','555-555-28327',
    'Joe Schmoe','');


--
-- Name: lnappschemadetail_detailid_seq; Type: SEQUENCE SET; Schema: public
--

-- SELECT pg_catalog.setval('public.lnappschemadetail_detailid_seq', 1181, true);


--
-- PostgreSQL database dump complete
--

