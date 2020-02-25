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
-- Data for Name: bsu_eformsschemamaster; Type: TABLE DATA; Schema: public; Owner: odyssey
--

INSERT INTO public.bsu_eformsschemamaster VALUES (4, 'DMSTEMPL', 'CU-CENTRIC - Template Real Estate', '', NULL);
INSERT INTO public.bsu_eformsschemamaster VALUES (5, 'DMSTEMPL', 'CU-CENTRIC - Template Open Ended', '', NULL);
INSERT INTO public.bsu_eformsschemamaster VALUES (6, 'DMSTEMPL', 'CU-CENTRIC - Template Closed Ended', '', NULL);
INSERT INTO public.bsu_eformsschemamaster VALUES (7, 'DMSTEMPL', 'CRUISE - ALL FIELDS LOAN APPLICATION', '', '2016-06-27');
INSERT INTO public.bsu_eformsschemamaster VALUES (8, 'DMSTEMPL', 'CRUISE - COMMON FIELDS LOAN APPLICATION', '', '2017-02-14');
INSERT INTO public.bsu_eformsschemamaster VALUES (10, 'DMSTEMPL', 'CUPRODIGY - SAMPLE APPLICATION', '', '2017-02-14');
INSERT INTO public.bsu_eformsschemamaster VALUES (1001, 'CRUISECU', 'Sample Loan Application', '', '2020-02-14');


--
-- Name: lnappschemamaster_loanid_seq; Type: SEQUENCE SET; Schema: public; Owner: odyssey
--

-- SELECT pg_catalog.setval('public.lnappschemamaster_loanid_seq', 1001, true);


--
-- PostgreSQL database dump complete
--

