PGDMP                       }            sql    16.9    17.5     I           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            J           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            K           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            L           1262    24600    sql    DATABASE     o   CREATE DATABASE sql WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.UTF-8';
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
       public               avnadmin    false    217            M           0    0    curso_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.curso_id_seq OWNED BY public.curso.id;
          public               avnadmin    false    218            �           2604    24623    curso id    DEFAULT     d   ALTER TABLE ONLY public.curso ALTER COLUMN id SET DEFAULT nextval('public.curso_id_seq'::regclass);
 7   ALTER TABLE public.curso ALTER COLUMN id DROP DEFAULT;
       public               avnadmin    false    218    217            E          0    24613    curso 
   TABLE DATA           M   COPY public.curso (nome, descricao, carga, total_aulas, ano, id) FROM stdin;
    public               avnadmin    false    217   
       N           0    0    curso_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.curso_id_seq', 20, true);
          public               avnadmin    false    218            �           2606    24621    curso curso_nome_key 
   CONSTRAINT     O   ALTER TABLE ONLY public.curso
    ADD CONSTRAINT curso_nome_key UNIQUE (nome);
 >   ALTER TABLE ONLY public.curso DROP CONSTRAINT curso_nome_key;
       public                 avnadmin    false    217            �           2606    24625    curso curso_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.curso
    ADD CONSTRAINT curso_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.curso DROP CONSTRAINT curso_pkey;
       public                 avnadmin    false    217            E   �   x�U�An�0EמS�b_%&)e��h��dD%6l�$��B&\���X�(���޼��s��"9�d^�t�(әP��E��P��Id���{�M�T2�}�w�\��m����څݓ���6�*ϻ���NR�(E�Yg��!��bЩ����,�/�%v��h�`K�;a ?�	�leP,j.�%�o�,�W1��C2�dc��E�{�_��a�     