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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: bsu_clientlist; Type: TABLE; Schema: public
--

CREATE TABLE public.bsu_clientlist (
    code character(10) NOT NULL,
    name character(40),
    addr1 character(40),
    addr2 character(40),
    city character(25),
    state character(15),
    zip character(15),
    email character(40),
    main_phone character(20),
    after_hours_phone character(20),
    ceo_mgr character(40),
    comments text
);


--
-- Name: bsu_eformsschemadetail; Type: TABLE; Schema: public
--

CREATE TABLE public.bsu_eformsschemadetail (
    detailid integer NOT NULL,
    loanid integer,
    pageid integer,
    groupid integer,
    lineid integer,
    fieldtype character varying(10),
    fieldvalue character varying(2000),
    fieldattr character varying(3000)
);


--
-- Name: bsu_eformsschemamaster; Type: TABLE; Schema: public
--

CREATE TABLE public.bsu_eformsschemamaster (
    loanid integer NOT NULL,
    code character varying(10),
    loantitle character varying(50),
    loandesc character varying(1000),
    lastmodified date
);


--
-- Name: bsu_officeusers; Type: TABLE; Schema: public
--

CREATE TABLE public.bsu_officeusers (
    user_name character varying(12) NOT NULL,
    password character varying(128) NOT NULL,
    failedremain integer DEFAULT 5,
    forceremain integer,
    last_login timestamp,
    priorlogin timestamp,
    failedlogin timestamp,
    pwchange timestamp with time zone,
    email character varying(100)
);


--
-- Name: eformsschemadetail_detailid_seq; Type: SEQUENCE; Schema: public
--

CREATE SEQUENCE public.eformsschemadetail_detailid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: eformsschemadetail_detailid_seq; Type: SEQUENCE OWNED BY; Schema: public
--

ALTER SEQUENCE public.eformsschemadetail_detailid_seq OWNED BY public.bsu_eformsschemadetail.detailid;


--
-- Name: eformsschemamaster_loanid_seq; Type: SEQUENCE; Schema: public
--

CREATE SEQUENCE public.eformsschemamaster_loanid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: eformsschemamaster_loanid_seq; Type: SEQUENCE OWNED BY; Schema: public
--

ALTER SEQUENCE public.eformsschemamaster_loanid_seq OWNED BY public.bsu_eformsschemamaster.loanid;


--
-- Name: bsu_eformsschemadetail detailid; Type: DEFAULT; Schema: public
--

ALTER TABLE ONLY public.bsu_eformsschemadetail ALTER COLUMN detailid SET DEFAULT nextval('public.eformsschemadetail_detailid_seq'::regclass);


--
-- Name: bsu_eformsschemamaster loanid; Type: DEFAULT; Schema: public
--

ALTER TABLE ONLY public.bsu_eformsschemamaster ALTER COLUMN loanid SET DEFAULT nextval('public.eformsschemamaster_loanid_seq'::regclass);


--
-- Name: bsu_clientlist clientlist_pkey; Type: CONSTRAINT; Schema: public
--

ALTER TABLE ONLY public.bsu_clientlist
    ADD CONSTRAINT clientlist_pkey PRIMARY KEY (code);


--
-- Name: bsu_officeusers officeusers_pkey; Type: CONSTRAINT; Schema: public
--

ALTER TABLE ONLY public.bsu_officeusers
    ADD CONSTRAINT officeusers_pkey PRIMARY KEY (user_name);


--
-- Name: clientlist_code_key; Type: INDEX; Schema: public
--

CREATE INDEX clientlist_code_key ON public.bsu_clientlist USING btree (code);


--
-- Name: eformsschemadetail_detailid_idx_01; Type: INDEX; Schema: public
--

CREATE UNIQUE INDEX eformsschemadetail_detailid_idx_01 ON public.bsu_eformsschemadetail USING btree (detailid);


--
-- Name: eformsschemamaster_loanid_idx01; Type: INDEX; Schema: public
--

CREATE UNIQUE INDEX eformsschemamaster_loanid_idx01 ON public.bsu_eformsschemamaster USING btree (loanid);


--
-- Name: officeusers_idx01; Type: INDEX; Schema: public
--

CREATE UNIQUE INDEX officeusers_idx01 ON public.bsu_officeusers USING btree (user_name);


--
-- PostgreSQL database dump complete
--

