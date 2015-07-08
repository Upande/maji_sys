--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: fews; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA fews;


ALTER SCHEMA fews OWNER TO postgres;

SET search_path = fews, pg_catalog;

--
-- Name: AggregationPeriods_aggregationperiodkey_seq; Type: SEQUENCE; Schema: fews; Owner: postgres
--

CREATE SEQUENCE "AggregationPeriods_aggregationperiodkey_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fews."AggregationPeriods_aggregationperiodkey_seq" OWNER TO postgres;

--
-- Name: Filters_filterkey_seq; Type: SEQUENCE; Schema: fews; Owner: postgres
--

CREATE SEQUENCE "Filters_filterkey_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fews."Filters_filterkey_seq" OWNER TO postgres;

--
-- Name: Locations_locationkey_seq; Type: SEQUENCE; Schema: fews; Owner: postgres
--

CREATE SEQUENCE "Locations_locationkey_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fews."Locations_locationkey_seq" OWNER TO postgres;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: locations; Type: TABLE; Schema: fews; Owner: postgres; Tablespace: 
--

CREATE TABLE locations (
    locationkey integer NOT NULL,
    id character varying(64) NOT NULL,
    name character varying(64),
    shortname character varying(64),
    description character varying(255),
    icon character varying(64),
    tooltip character varying(64),
    parentlocationid character varying(64),
    visibilitystarttime timestamp without time zone,
    visibilityendtime timestamp without time zone,
    x double precision NOT NULL,
    y double precision NOT NULL,
    z double precision,
    wgs_geom public.geometry,
    area double precision,
    relationalocationid character varying(64),
    relationblocationid character varying(64),
    attributea character varying(64),
    attributeb double precision,
    rainfall boolean,
    lake_level character varying(1),
    harmax_h double precision,
    harmin_h double precision
);


ALTER TABLE fews.locations OWNER TO postgres;

--
-- Name: COLUMN locations.wgs_geom; Type: COMMENT; Schema: fews; Owner: postgres
--

COMMENT ON COLUMN locations.wgs_geom IS 'geometery in 21037';


--
-- Name: Locations_locationkey_seq1; Type: SEQUENCE; Schema: fews; Owner: postgres
--

CREATE SEQUENCE "Locations_locationkey_seq1"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fews."Locations_locationkey_seq1" OWNER TO postgres;

--
-- Name: Locations_locationkey_seq1; Type: SEQUENCE OWNED BY; Schema: fews; Owner: postgres
--

ALTER SEQUENCE "Locations_locationkey_seq1" OWNED BY locations.locationkey;


--
-- Name: ModuleInstances_moduleinstancekey_seq; Type: SEQUENCE; Schema: fews; Owner: postgres
--

CREATE SEQUENCE "ModuleInstances_moduleinstancekey_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fews."ModuleInstances_moduleinstancekey_seq" OWNER TO postgres;

--
-- Name: ParameterGroups_groupkey_seq; Type: SEQUENCE; Schema: fews; Owner: postgres
--

CREATE SEQUENCE "ParameterGroups_groupkey_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fews."ParameterGroups_groupkey_seq" OWNER TO postgres;

--
-- Name: ParametersTable_parameterkey_seq; Type: SEQUENCE; Schema: fews; Owner: postgres
--

CREATE SEQUENCE "ParametersTable_parameterkey_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fews."ParametersTable_parameterkey_seq" OWNER TO postgres;

--
-- Name: QualifierSets_qualifiersetkey_seq; Type: SEQUENCE; Schema: fews; Owner: postgres
--

CREATE SEQUENCE "QualifierSets_qualifiersetkey_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fews."QualifierSets_qualifiersetkey_seq" OWNER TO postgres;

--
-- Name: Qualifiers_qualifierkey_seq; Type: SEQUENCE; Schema: fews; Owner: postgres
--

CREATE SEQUENCE "Qualifiers_qualifierkey_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fews."Qualifiers_qualifierkey_seq" OWNER TO postgres;

--
-- Name: TimeSeriesKeys_serieskey_seq; Type: SEQUENCE; Schema: fews; Owner: postgres
--

CREATE SEQUENCE "TimeSeriesKeys_serieskey_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fews."TimeSeriesKeys_serieskey_seq" OWNER TO postgres;

--
-- Name: TimeSteps_timestepkey_seq; Type: SEQUENCE; Schema: fews; Owner: postgres
--

CREATE SEQUENCE "TimeSteps_timestepkey_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fews."TimeSteps_timestepkey_seq" OWNER TO postgres;

--
-- Name: Users_userkey_seq; Type: SEQUENCE; Schema: fews; Owner: postgres
--

CREATE SEQUENCE "Users_userkey_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fews."Users_userkey_seq" OWNER TO postgres;

--
-- Name: aggregationperiods; Type: TABLE; Schema: fews; Owner: postgres; Tablespace: 
--

CREATE TABLE aggregationperiods (
    aggregationperiodkey integer DEFAULT nextval('"AggregationPeriods_aggregationperiodkey_seq"'::regclass) NOT NULL,
    id character varying(64) NOT NULL,
    description character varying(255)
);


ALTER TABLE fews.aggregationperiods OWNER TO postgres;

--
-- Name: dual; Type: VIEW; Schema: fews; Owner: postgres
--

CREATE VIEW dual AS
 SELECT ('now'::text)::date AS date;


ALTER TABLE fews.dual OWNER TO postgres;

--
-- Name: filters; Type: TABLE; Schema: fews; Owner: postgres; Tablespace: 
--

CREATE TABLE filters (
    filterkey integer DEFAULT nextval('"Filters_filterkey_seq"'::regclass) NOT NULL,
    id character varying(64) NOT NULL,
    name character varying(64),
    description character varying(255),
    parentfilterid character varying(64),
    validationiconsvisible integer NOT NULL,
    mapextentid character varying(64),
    viewpermission character varying(64),
    editpermission character varying(64)
);


ALTER TABLE fews.filters OWNER TO postgres;

--
-- Name: filtertimeserieskeys; Type: TABLE; Schema: fews; Owner: postgres; Tablespace: 
--

CREATE TABLE filtertimeserieskeys (
    filterkey integer NOT NULL,
    serieskey integer NOT NULL
);


ALTER TABLE fews.filtertimeserieskeys OWNER TO postgres;

--
-- Name: moduleinstances; Type: TABLE; Schema: fews; Owner: postgres; Tablespace: 
--

CREATE TABLE moduleinstances (
    moduleinstancekey integer DEFAULT nextval('"ModuleInstances_moduleinstancekey_seq"'::regclass) NOT NULL,
    id character varying(64) NOT NULL,
    name character varying(64),
    description character varying(255)
);


ALTER TABLE fews.moduleinstances OWNER TO postgres;

--
-- Name: parametergroups; Type: TABLE; Schema: fews; Owner: postgres; Tablespace: 
--

CREATE TABLE parametergroups (
    groupkey integer DEFAULT nextval('"ParameterGroups_groupkey_seq"'::regclass) NOT NULL,
    id character varying(64) NOT NULL,
    name character varying(64),
    description character varying(255),
    parametertype character varying(64) NOT NULL,
    unit character varying(64),
    displayunit character varying(64)
);


ALTER TABLE fews.parametergroups OWNER TO postgres;

--
-- Name: parameterstable; Type: TABLE; Schema: fews; Owner: postgres; Tablespace: 
--

CREATE TABLE parameterstable (
    parameterkey integer DEFAULT nextval('"ParametersTable_parameterkey_seq"'::regclass) NOT NULL,
    groupkey integer NOT NULL,
    id character varying(64) NOT NULL,
    name character varying(64),
    shortname character varying(64),
    description character varying(255),
    valueresolution double precision,
    attributea character varying(64),
    attributeb double precision
);


ALTER TABLE fews.parameterstable OWNER TO postgres;

--
-- Name: qualifiers; Type: TABLE; Schema: fews; Owner: postgres; Tablespace: 
--

CREATE TABLE qualifiers (
    qualifierkey integer DEFAULT nextval('"Qualifiers_qualifierkey_seq"'::regclass) NOT NULL,
    id character varying(64) NOT NULL,
    name character varying(64),
    shortname character varying(64),
    description character varying(255)
);


ALTER TABLE fews.qualifiers OWNER TO postgres;

--
-- Name: qualifiersets; Type: TABLE; Schema: fews; Owner: postgres; Tablespace: 
--

CREATE TABLE qualifiersets (
    qualifiersetkey integer DEFAULT nextval('"QualifierSets_qualifiersetkey_seq"'::regclass) NOT NULL,
    id character varying(64) NOT NULL,
    qualifierkey1 integer NOT NULL,
    qualifierkey2 integer,
    qualifierkey3 integer,
    qualifierkey4 integer
);


ALTER TABLE fews.qualifiersets OWNER TO postgres;

--
-- Name: samples; Type: TABLE; Schema: fews; Owner: postgres; Tablespace: 
--

CREATE TABLE samples (
    locationkey integer NOT NULL,
    datetime timestamp without time zone NOT NULL,
    id character varying(64) NOT NULL,
    description character varying(255)
);


ALTER TABLE fews.samples OWNER TO postgres;

--
-- Name: timeseriescomments; Type: TABLE; Schema: fews; Owner: postgres; Tablespace: 
--

CREATE TABLE timeseriescomments (
    serieskey integer NOT NULL,
    datetime timestamp without time zone NOT NULL,
    commenttext character varying(64) NOT NULL
);


ALTER TABLE fews.timeseriescomments OWNER TO postgres;

--
-- Name: timeserieskeys; Type: TABLE; Schema: fews; Owner: postgres; Tablespace: 
--

CREATE TABLE timeserieskeys (
    serieskey integer DEFAULT nextval('"TimeSeriesKeys_serieskey_seq"'::regclass) NOT NULL,
    locationkey integer NOT NULL,
    parameterkey integer NOT NULL,
    qualifiersetkey integer,
    moduleinstancekey integer NOT NULL,
    timestepkey integer NOT NULL,
    aggregationperiodkey integer,
    valuetype integer DEFAULT 0 NOT NULL,
    modificationtime timestamp without time zone NOT NULL
);


ALTER TABLE fews.timeserieskeys OWNER TO postgres;

--
-- Name: timeseriesmanualeditshistory; Type: TABLE; Schema: fews; Owner: postgres; Tablespace: 
--

CREATE TABLE timeseriesmanualeditshistory (
    serieskey integer NOT NULL,
    editdatetime timestamp without time zone NOT NULL,
    datetime timestamp without time zone NOT NULL,
    userkey integer,
    scalarvalue double precision,
    flags integer NOT NULL,
    commenttext character varying(64),
    id integer
);


ALTER TABLE fews.timeseriesmanualeditshistory OWNER TO postgres;

--
-- Name: timeseriesvaluesandflags; Type: TABLE; Schema: fews; Owner: postgres; Tablespace: 
--

CREATE TABLE timeseriesvaluesandflags (
    serieskey integer NOT NULL,
    datetime timestamp without time zone NOT NULL,
    scalarvalue double precision,
    flags integer NOT NULL
);


ALTER TABLE fews.timeseriesvaluesandflags OWNER TO postgres;

--
-- Name: timesteps; Type: TABLE; Schema: fews; Owner: postgres; Tablespace: 
--

CREATE TABLE timesteps (
    timestepkey integer DEFAULT nextval('"TimeSteps_timestepkey_seq"'::regclass) NOT NULL,
    id character varying(64) NOT NULL,
    label character varying(64)
);


ALTER TABLE fews.timesteps OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: fews; Owner: postgres; Tablespace: 
--

CREATE TABLE users (
    userkey integer DEFAULT nextval('"Users_userkey_seq"'::regclass) NOT NULL,
    id character varying(64) NOT NULL,
    name character varying(64)
);


ALTER TABLE fews.users OWNER TO postgres;

--
-- Name: locationkey; Type: DEFAULT; Schema: fews; Owner: postgres
--

ALTER TABLE ONLY locations ALTER COLUMN locationkey SET DEFAULT nextval('"Locations_locationkey_seq1"'::regclass);


--
-- Name: pk_aggregationper; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY aggregationperiods
    ADD CONSTRAINT pk_aggregationper PRIMARY KEY (aggregationperiodkey);


--
-- Name: pk_filters; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY filters
    ADD CONSTRAINT pk_filters PRIMARY KEY (filterkey);


--
-- Name: pk_filtertimeseriesk; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY filtertimeserieskeys
    ADD CONSTRAINT pk_filtertimeseriesk PRIMARY KEY (filterkey, serieskey);


--
-- Name: pk_locations; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY locations
    ADD CONSTRAINT pk_locations PRIMARY KEY (locationkey);


--
-- Name: pk_moduleinstances; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY moduleinstances
    ADD CONSTRAINT pk_moduleinstances PRIMARY KEY (moduleinstancekey);


--
-- Name: pk_parametergroups; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY parametergroups
    ADD CONSTRAINT pk_parametergroups PRIMARY KEY (groupkey);


--
-- Name: pk_parameterstable; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY parameterstable
    ADD CONSTRAINT pk_parameterstable PRIMARY KEY (parameterkey);


--
-- Name: pk_qualifiers; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY qualifiers
    ADD CONSTRAINT pk_qualifiers PRIMARY KEY (qualifierkey);


--
-- Name: pk_qualifiersets; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY qualifiersets
    ADD CONSTRAINT pk_qualifiersets PRIMARY KEY (qualifiersetkey);


--
-- Name: pk_samples; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY samples
    ADD CONSTRAINT pk_samples PRIMARY KEY (locationkey, datetime);


--
-- Name: pk_timeseriescomments; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY timeseriescomments
    ADD CONSTRAINT pk_timeseriescomments PRIMARY KEY (serieskey, datetime);


--
-- Name: pk_timeserieskeys; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY timeserieskeys
    ADD CONSTRAINT pk_timeserieskeys PRIMARY KEY (serieskey);


--
-- Name: pk_timeseriesmanualedits; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY timeseriesmanualeditshistory
    ADD CONSTRAINT pk_timeseriesmanualedits PRIMARY KEY (serieskey, datetime, editdatetime);


--
-- Name: pk_timeseriesvaluesandflags; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY timeseriesvaluesandflags
    ADD CONSTRAINT pk_timeseriesvaluesandflags PRIMARY KEY (serieskey, datetime);


--
-- Name: pk_timesteps; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY timesteps
    ADD CONSTRAINT pk_timesteps PRIMARY KEY (timestepkey);


--
-- Name: pk_users; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT pk_users PRIMARY KEY (userkey);


--
-- Name: uniq_aggregationper_id; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY aggregationperiods
    ADD CONSTRAINT uniq_aggregationper_id UNIQUE (id);


--
-- Name: uniq_filters_id; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY filters
    ADD CONSTRAINT uniq_filters_id UNIQUE (id);


--
-- Name: uniq_locations_id; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY locations
    ADD CONSTRAINT uniq_locations_id UNIQUE (id);


--
-- Name: uniq_moduleinstances_id; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY moduleinstances
    ADD CONSTRAINT uniq_moduleinstances_id UNIQUE (id);


--
-- Name: uniq_parametergroups_id; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY parametergroups
    ADD CONSTRAINT uniq_parametergroups_id UNIQUE (id);


--
-- Name: uniq_parameterstable_id; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY parameterstable
    ADD CONSTRAINT uniq_parameterstable_id UNIQUE (id);


--
-- Name: uniq_qualifiers_id; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY qualifiers
    ADD CONSTRAINT uniq_qualifiers_id UNIQUE (id);


--
-- Name: uniq_qualifiersets_id; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY qualifiersets
    ADD CONSTRAINT uniq_qualifiersets_id UNIQUE (id);


--
-- Name: uniq_timeserieskey_compound; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY timeserieskeys
    ADD CONSTRAINT uniq_timeserieskey_compound UNIQUE (locationkey, parameterkey, qualifiersetkey, moduleinstancekey, timestepkey, aggregationperiodkey);


--
-- Name: uniq_timesteps_id; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY timesteps
    ADD CONSTRAINT uniq_timesteps_id UNIQUE (id);


--
-- Name: uniq_users_id; Type: CONSTRAINT; Schema: fews; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT uniq_users_id UNIQUE (id);


--
-- Name: fk_filtertimeseriesk_filterkey; Type: FK CONSTRAINT; Schema: fews; Owner: postgres
--

ALTER TABLE ONLY filtertimeserieskeys
    ADD CONSTRAINT fk_filtertimeseriesk_filterkey FOREIGN KEY (filterkey) REFERENCES filters(filterkey);


--
-- Name: fk_filtertimeseriesk_serieskey; Type: FK CONSTRAINT; Schema: fews; Owner: postgres
--

ALTER TABLE ONLY filtertimeserieskeys
    ADD CONSTRAINT fk_filtertimeseriesk_serieskey FOREIGN KEY (serieskey) REFERENCES timeserieskeys(serieskey);


--
-- Name: fk_parameterst_groupkey; Type: FK CONSTRAINT; Schema: fews; Owner: postgres
--

ALTER TABLE ONLY parameterstable
    ADD CONSTRAINT fk_parameterst_groupkey FOREIGN KEY (groupkey) REFERENCES parametergroups(groupkey);


--
-- Name: fk_qualifiersets_qualifierkey1; Type: FK CONSTRAINT; Schema: fews; Owner: postgres
--

ALTER TABLE ONLY qualifiersets
    ADD CONSTRAINT fk_qualifiersets_qualifierkey1 FOREIGN KEY (qualifierkey1) REFERENCES qualifiers(qualifierkey);


--
-- Name: fk_qualifiersets_qualifierkey2; Type: FK CONSTRAINT; Schema: fews; Owner: postgres
--

ALTER TABLE ONLY qualifiersets
    ADD CONSTRAINT fk_qualifiersets_qualifierkey2 FOREIGN KEY (qualifierkey2) REFERENCES qualifiers(qualifierkey);


--
-- Name: fk_qualifiersets_qualifierkey3; Type: FK CONSTRAINT; Schema: fews; Owner: postgres
--

ALTER TABLE ONLY qualifiersets
    ADD CONSTRAINT fk_qualifiersets_qualifierkey3 FOREIGN KEY (qualifierkey3) REFERENCES qualifiers(qualifierkey);


--
-- Name: fk_qualifiersets_qualifierkey4; Type: FK CONSTRAINT; Schema: fews; Owner: postgres
--

ALTER TABLE ONLY qualifiersets
    ADD CONSTRAINT fk_qualifiersets_qualifierkey4 FOREIGN KEY (qualifierkey4) REFERENCES qualifiers(qualifierkey);


--
-- Name: fk_timeseriescomments; Type: FK CONSTRAINT; Schema: fews; Owner: postgres
--

ALTER TABLE ONLY timeseriescomments
    ADD CONSTRAINT fk_timeseriescomments FOREIGN KEY (serieskey) REFERENCES timeserieskeys(serieskey);


--
-- Name: fk_timeserieskeys_aggperkey; Type: FK CONSTRAINT; Schema: fews; Owner: postgres
--

ALTER TABLE ONLY timeserieskeys
    ADD CONSTRAINT fk_timeserieskeys_aggperkey FOREIGN KEY (aggregationperiodkey) REFERENCES aggregationperiods(aggregationperiodkey);


--
-- Name: fk_timeserieskeys_modinskey; Type: FK CONSTRAINT; Schema: fews; Owner: postgres
--

ALTER TABLE ONLY timeserieskeys
    ADD CONSTRAINT fk_timeserieskeys_modinskey FOREIGN KEY (moduleinstancekey) REFERENCES moduleinstances(moduleinstancekey);


--
-- Name: fk_timeserieskeys_paramkey; Type: FK CONSTRAINT; Schema: fews; Owner: postgres
--

ALTER TABLE ONLY timeserieskeys
    ADD CONSTRAINT fk_timeserieskeys_paramkey FOREIGN KEY (parameterkey) REFERENCES parameterstable(parameterkey);


--
-- Name: fk_timeserieskeys_qualsetkey; Type: FK CONSTRAINT; Schema: fews; Owner: postgres
--

ALTER TABLE ONLY timeserieskeys
    ADD CONSTRAINT fk_timeserieskeys_qualsetkey FOREIGN KEY (qualifiersetkey) REFERENCES qualifiersets(qualifiersetkey);


--
-- Name: fk_timeserieskeys_timestepkey; Type: FK CONSTRAINT; Schema: fews; Owner: postgres
--

ALTER TABLE ONLY timeserieskeys
    ADD CONSTRAINT fk_timeserieskeys_timestepkey FOREIGN KEY (timestepkey) REFERENCES timesteps(timestepkey);


--
-- Name: fk_timeseriesmane_serieskey; Type: FK CONSTRAINT; Schema: fews; Owner: postgres
--

ALTER TABLE ONLY timeseriesmanualeditshistory
    ADD CONSTRAINT fk_timeseriesmane_serieskey FOREIGN KEY (serieskey) REFERENCES timeserieskeys(serieskey);


--
-- Name: fk_timeseriesvaluesandflags; Type: FK CONSTRAINT; Schema: fews; Owner: postgres
--

ALTER TABLE ONLY timeseriesvaluesandflags
    ADD CONSTRAINT fk_timeseriesvaluesandflags FOREIGN KEY (serieskey) REFERENCES timeserieskeys(serieskey);


--
-- PostgreSQL database dump complete
--

