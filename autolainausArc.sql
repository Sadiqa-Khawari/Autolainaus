
CREATE TABLE public.ajoneuvotyyppi (
                tyyppi VARCHAR(30) NOT NULL,
                CONSTRAINT ajoneuvotyyppi_pk PRIMARY KEY (tyyppi)
);


CREATE TABLE public.auto (
                rekisterinumero VARCHAR(7) NOT NULL,
                kaytettavissa BOOLEAN DEFAULT TRUE NOT NULL,
                merkki VARCHAR(30) NOT NULL,
                Malli VARCHAR(30) NOT NULL,
                vuosimalli CHAR(4) NOT NULL,
                henkilomaara INTEGER NOT NULL,
                tyyppi VARCHAR(30) NOT NULL,
                automaatti BOOLEAN NOT NULL,
                vastuuhenkilo VARCHAR(30),
                kuva BYTEA,
                CONSTRAINT auto_pk PRIMARY KEY (rekisterinumero)
);


CREATE TABLE public.lainaaja (
                hetu VARCHAR(11) NOT NULL,
                etunimi VARCHAR(50) NOT NULL,
                sukunimi VARCHAR(50) NOT NULL,
                ajokorttiluokka VARCHAR(10) NOT NULL,
                automaatti BOOLEAN NOT NULL,
                sahkoposti VARCHAR(50),
                CONSTRAINT lainaaja_pk PRIMARY KEY (hetu)
);


CREATE TABLE public.tarkoitus (
                tarkoitus VARCHAR(30) NOT NULL,
                CONSTRAINT tarkoitus_pk PRIMARY KEY (tarkoitus)
);


CREATE SEQUENCE public.lainaus_lainausnumero_seq;

CREATE TABLE public.lainaus (
                lainausnumero INTEGER NOT NULL DEFAULT nextval('public.lainaus_lainausnumero_seq'),
                tarkoitus VARCHAR(30) NOT NULL,
                hetu VARCHAR(11) NOT NULL,
                rekisterinumero VARCHAR(7) NOT NULL,
                lainausaika TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                palautusaika TIMESTAMP,
                CONSTRAINT lainaus_pk PRIMARY KEY (lainausnumero)
);


ALTER SEQUENCE public.lainaus_lainausnumero_seq OWNED BY public.lainaus.lainausnumero;

ALTER TABLE public.auto ADD CONSTRAINT ajoneuvotyyppi_auto_fk
FOREIGN KEY (tyyppi)
REFERENCES public.ajoneuvotyyppi (tyyppi)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.lainaus ADD CONSTRAINT auto_lainaus_fk
FOREIGN KEY (rekisterinumero)
REFERENCES public.auto (rekisterinumero)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.lainaus ADD CONSTRAINT lainaaja_lainaus_fk
FOREIGN KEY (hetu)
REFERENCES public.lainaaja (hetu)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.lainaus ADD CONSTRAINT tarkoitus_lainaus_fk
FOREIGN KEY (tarkoitus)
REFERENCES public.tarkoitus (tarkoitus)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
