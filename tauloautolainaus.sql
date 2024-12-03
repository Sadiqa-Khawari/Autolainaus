
CREATE TABLE auto (
                rekisterinumero VARCHAR(7) NOT NULL,
                merkki VARCHAR(30) NOT NULL,
                malli VARCHAR(20) NOT NULL,
                vuosimalli VARCHAR(4) NOT NULL,
                CONSTRAINT auto_pk PRIMARY KEY (rekisterinumero)
);
COMMENT ON TABLE auto IS 'Ajaneuvon perostiedot';


CREATE TABLE ryhma (
                ryhma VARCHAR(50) NOT NULL,
                vastuhenkil VARCHAR(50),
                CONSTRAINT ryhma_pk PRIMARY KEY (ryhma)
);
COMMENT ON TABLE ryhma IS 'Opiskelijan luokka';
COMMENT ON COLUMN ryhma.ryhma IS 'Ryhm�n nimi, esim. auto22B henkil�kunta';
COMMENT ON COLUMN ryhma.vastuhenkil IS 'Vastuopettaja';


CREATE TABLE lainaaja (
                hetu CHAR(11) NOT NULL,
                sahkoposti VARCHAR(30) NOT NULL,
                etunimi VARCHAR(50) NOT NULL,
                sukunimi VARCHAR(50) NOT NULL,
                ryhma VARCHAR(50) NOT NULL,
                ajakorttiluokka VARCHAR(6) NOT NULL,
                CONSTRAINT lainaaja_pk PRIMARY KEY (hetu)
);
COMMENT ON TABLE lainaaja IS 'lainaajan (opiskelija tai ope)
perustiedot';
COMMENT ON COLUMN lainaaja.hetu IS 'Kansallinen henkil�tunnus';
COMMENT ON COLUMN lainaaja.sahkoposti IS 'Raseko s�hk�posti';
COMMENT ON COLUMN lainaaja.ryhma IS 'Ryhm�n nimi, esim. auto22B henkil�kunta';
COMMENT ON COLUMN lainaaja.ajakorttiluokka IS 'Esim AB tai ABCE';


CREATE TABLE lainaus (
                lainausnumero INTEGER NOT NULL,
                palautus TIMESTAMP,
                hetu CHAR(11) NOT NULL,
                rekisterinumero VARCHAR(7) NOT NULL,
                lainausaika TIMESTAMP NOT NULL,
                CONSTRAINT lainaus_pk PRIMARY KEY (lainausnumero)
);
COMMENT ON TABLE lainaus IS 'Lainaustapahtuman tiedot';
COMMENT ON COLUMN lainaus.lainausnumero IS 'Lainaustapahtumalle automaattisesti annettava';
COMMENT ON COLUMN lainaus.palautus IS 'Palautuksen p�iv� ja kelloaika';
COMMENT ON COLUMN lainaus.hetu IS 'Kansallinen henkil�tunnus';
COMMENT ON COLUMN lainaus.lainausaika IS 'P�iv�m��r� ja kelloaika, kun auto on ';


ALTER TABLE lainaus ADD CONSTRAINT auto_lainaus_fk
FOREIGN KEY (rekisterinumero)
REFERENCES auto (rekisterinumero)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE lainaaja ADD CONSTRAINT ryhma_lainaaja_fk
FOREIGN KEY (ryhma)
REFERENCES ryhma (ryhma)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE lainaus ADD CONSTRAINT lainaaja_lainaus_fk
FOREIGN KEY (hetu)
REFERENCES lainaaja (hetu)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
