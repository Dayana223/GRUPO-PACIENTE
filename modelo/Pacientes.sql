PGDMP              	        |         	   Pacientes    16.3    16.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16398 	   Pacientes    DATABASE     ~   CREATE DATABASE "Pacientes" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Spain.1252';
    DROP DATABASE "Pacientes";
                postgres    false            �            1259    16399    Paciente    TABLE     �   CREATE TABLE public."Paciente" (
    dni_paciente integer NOT NULL,
    nombre_paciente character varying(100) NOT NULL,
    turno_prox_paciente character varying(100) NOT NULL,
    apellido_paciente character varying NOT NULL
);
    DROP TABLE public."Paciente";
       public         heap    postgres    false            �          0    16399    Paciente 
   TABLE DATA           k   COPY public."Paciente" (dni_paciente, nombre_paciente, turno_prox_paciente, apellido_paciente) FROM stdin;
    public          postgres    false    215                     2606    16405    Paciente Paciente_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public."Paciente"
    ADD CONSTRAINT "Paciente_pkey" PRIMARY KEY (dni_paciente);
 D   ALTER TABLE ONLY public."Paciente" DROP CONSTRAINT "Paciente_pkey";
       public            postgres    false    215            �      x������ � �     