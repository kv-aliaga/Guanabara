PGDMP                       }            sql    16.9    17.5     S           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            T           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            U           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            V           1262    24600    sql    DATABASE     o   CREATE DATABASE sql WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.UTF-8';
    DROP DATABASE sql;
                     avnadmin    false            �            1259    24613    curso    TABLE     �   CREATE TABLE public.curso (
    nome character varying(10) NOT NULL,
    descricao text,
    carga integer,
    total_aulas integer,
    ano integer DEFAULT 2025,
    id integer NOT NULL,
    CONSTRAINT curso_carga_check CHECK ((carga >= 0))
);
    DROP TABLE public.curso;
       public         heap r       avnadmin    false            �            1259    24622    curso_id_seq    SEQUENCE     �   CREATE SEQUENCE public.curso_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.curso_id_seq;
       public               avnadmin    false    217            W           0    0    curso_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.curso_id_seq OWNED BY public.curso.id;
          public               avnadmin    false    218            �            1259    24603    pessoa    TABLE     �  CREATE TABLE public.pessoa (
    id integer NOT NULL,
    nome character varying(30) NOT NULL,
    nascimento date,
    genero character(1),
    peso numeric(5,2),
    altura numeric(3,2),
    nacionalidade character varying(30) DEFAULT 'Brasil'::character varying,
    emprego character varying(20) DEFAULT 'desempregado'::character varying,
    CONSTRAINT pessoas_genero_check CHECK ((genero = ANY (ARRAY['M'::bpchar, 'F'::bpchar])))
);
    DROP TABLE public.pessoa;
       public         heap r       avnadmin    false            �            1259    24602    pessoas_id_seq    SEQUENCE     �   CREATE SEQUENCE public.pessoas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.pessoas_id_seq;
       public               avnadmin    false    216            X           0    0    pessoas_id_seq    SEQUENCE OWNED BY     @   ALTER SEQUENCE public.pessoas_id_seq OWNED BY public.pessoa.id;
          public               avnadmin    false    215            �           2604    24623    curso id    DEFAULT     d   ALTER TABLE ONLY public.curso ALTER COLUMN id SET DEFAULT nextval('public.curso_id_seq'::regclass);
 7   ALTER TABLE public.curso ALTER COLUMN id DROP DEFAULT;
       public               avnadmin    false    218    217            �           2604    24606 	   pessoa id    DEFAULT     g   ALTER TABLE ONLY public.pessoa ALTER COLUMN id SET DEFAULT nextval('public.pessoas_id_seq'::regclass);
 8   ALTER TABLE public.pessoa ALTER COLUMN id DROP DEFAULT;
       public               avnadmin    false    215    216    216            O          0    24613    curso 
   TABLE DATA           M   COPY public.curso (nome, descricao, carga, total_aulas, ano, id) FROM stdin;
    public               avnadmin    false    217   �       N          0    24603    pessoa 
   TABLE DATA           d   COPY public.pessoa (id, nome, nascimento, genero, peso, altura, nacionalidade, emprego) FROM stdin;
    public               avnadmin    false    216   �       Y           0    0    curso_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.curso_id_seq', 20, true);
          public               avnadmin    false    218            Z           0    0    pessoas_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.pessoas_id_seq', 5, true);
          public               avnadmin    false    215            �           2606    24621    curso curso_nome_key 
   CONSTRAINT     O   ALTER TABLE ONLY public.curso
    ADD CONSTRAINT curso_nome_key UNIQUE (nome);
 >   ALTER TABLE ONLY public.curso DROP CONSTRAINT curso_nome_key;
       public                 avnadmin    false    217            �           2606    24625    curso curso_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.curso
    ADD CONSTRAINT curso_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.curso DROP CONSTRAINT curso_pkey;
       public                 avnadmin    false    217            �           2606    24610    pessoa pessoas_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.pessoa
    ADD CONSTRAINT pessoas_pkey PRIMARY KEY (id);
 =   ALTER TABLE ONLY public.pessoa DROP CONSTRAINT pessoas_pkey;
       public                 avnadmin    false    216            O   �   x�U�An�0EמS�b_%&)e��h��dD%6l�$��B&\���X�(���޼��s��"9�d^�t�(әP��E��P��Id���{�M�T2�}�w�\��m����څݓ���6�*ϻ���NR�(E�Yg��!��bЩ����,�/�%v��h�`K�;a ?�	�leP,j.�%�o�,�W1��C2�dc��E�{�_��a�      N   �   x��α
�0����]nb��ZTPpqv���)����Z��p֏�h���i�d�q���"�V[B����/�>e�O��03�H��pD�>®��q	z��J[W+��r���3��{��_�,�ȋpR�׹E�uqSB�'AD�     