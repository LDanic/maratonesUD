/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 16.1 		*/
/*  Created On : 23-nov.-2023 8:51:16 a. m. 				*/
/*  DBMS       : PostgreSQL 						*/
/* ---------------------------------------------------- */

/* Drop Sequences for Autonumber Columns */

DROP SEQUENCE IF EXISTS competencia_id_competencia_seq
;

DROP SEQUENCE IF EXISTS equipo_id_equipo_seq
;

/* Drop Tables */

DROP TABLE IF EXISTS Competencia CASCADE
;

DROP TABLE IF EXISTS Equipo CASCADE
;

DROP TABLE IF EXISTS Estudiante CASCADE
;

/* Create Tables */

CREATE TABLE Competencia
(
	id_competencia smallint NOT NULL   DEFAULT NEXTVAL(('competencia_id_competencia_seq'::text)::regclass),	-- identificador del equipo
	categoria varchar(50) NOT NULL,	-- categoria de la competencia 
	semestre varchar(6) NOT NULL	-- semestre en que se realiza la competencia
)
;

CREATE TABLE Equipo
(
	id_equipo smallint NOT NULL   DEFAULT NEXTVAL(('equipo_id_equipo_seq'::text)::regclass),	-- identificador del equipo
	nom_equipo varchar(50) NOT NULL,	-- nombre del equipo
	id_competencia smallint NOT NULL
)
;

CREATE TABLE Estudiante
(
	codigo_est bigint NOT NULL,	-- Codigo estudiantil
	nom_est varchar(50) NOT NULL,	-- nombre del estudiante
	ape_est varchar(50) NOT NULL,	-- apellido del estudiante
	carrera varchar(50) NOT NULL,	-- carrera del estudiante
	materia_programacion varchar(50) NOT NULL,	-- materia mas avanzada de programacion que este viendo es estudiante
	id_equipo smallint NOT NULL	-- id del equipo al que pertenece el estudiante
)
;

/* Create Primary Keys, Indexes, Uniques, Checks */

ALTER TABLE Competencia ADD CONSTRAINT PK_Competencia
	PRIMARY KEY (id_competencia)
;

ALTER TABLE Competencia ADD CONSTRAINT check_categoria CHECK (categoria IN ('basica', 'intermedia', 'avanzada', 'elite'))
;

ALTER TABLE Equipo ADD CONSTRAINT PK_Equipo
	PRIMARY KEY (id_equipo)
;

ALTER TABLE Estudiante ADD CONSTRAINT PK_Estudiante
	PRIMARY KEY (codigo_est)
;

/* Create Foreign Key Constraints */

ALTER TABLE Equipo ADD CONSTRAINT FK_Equipo_Competencia
	FOREIGN KEY (id_competencia) REFERENCES Competencia (id_competencia) ON DELETE No Action ON UPDATE No Action
;

ALTER TABLE Estudiante ADD CONSTRAINT FK_Estudiante_Equipo
	FOREIGN KEY (id_equipo) REFERENCES Equipo (id_equipo) ON DELETE No Action ON UPDATE No Action
;

/* Create Table Comments, Sequences for Autonumber Columns */

COMMENT ON COLUMN Competencia.id_competencia
	IS 'identificador del equipo'
;

COMMENT ON COLUMN Competencia.categoria
	IS 'categoria de la competencia '
;

COMMENT ON COLUMN Competencia.semestre
	IS 'semestre en que se realiza la competencia'
;

CREATE SEQUENCE competencia_id_competencia_seq INCREMENT 1 START 1
;

COMMENT ON COLUMN Equipo.id_equipo
	IS 'identificador del equipo'
;

COMMENT ON COLUMN Equipo.nom_equipo
	IS 'nombre del equipo'
;

CREATE SEQUENCE equipo_id_equipo_seq INCREMENT 1 START 1
;

COMMENT ON COLUMN Estudiante.codigo_est
	IS 'Codigo estudiantil'
;

COMMENT ON COLUMN Estudiante.nom_est
	IS 'nombre del estudiante'
;

COMMENT ON COLUMN Estudiante.ape_est
	IS 'apellido del estudiante'
;

COMMENT ON COLUMN Estudiante.carrera
	IS 'carrera del estudiante'
;

COMMENT ON COLUMN Estudiante.materia_programacion
	IS 'materia mas avanzada de programacion que este viendo es estudiante'
;

COMMENT ON COLUMN Estudiante.id_equipo
	IS 'id del equipo al que pertenece el estudiante'
;
