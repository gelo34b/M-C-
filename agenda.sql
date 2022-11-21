-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-11-2022 a las 05:36:29
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `agenda`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clases`
--

CREATE TABLE `clases` (
  `idclase` int(11) NOT NULL,
  `nomclase` varchar(70) NOT NULL,
  `nomprofesor` varchar(70) NOT NULL,
  `horario` varchar(70) NOT NULL,
  `precio` varchar(10) NOT NULL,
  `instru` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `clases`
--

INSERT INTO `clases` (`idclase`, `nomclase`, `nomprofesor`, `horario`, `precio`, `instru`) VALUES
(7, 'Clase de Guitarra', 'Luis Armando', 'De Lunes a Martes de 2:00 p.m. a 3:00 p.m.', '130', 'Si'),
(25, 'Clase de violin', 'Carlos Sanchez', 'De Lunes a Martes de 2:00 p.m. a 3:00 p.m.', '130 ', 'si'),
(26, 'Clase de Bateria ', 'Juan Luis', 'De Lunes a Martes de 2:00 p.m. a 3:00 p.m.', '180', 'si'),
(27, 'Clase de Bateria ', 'Marco Salas', 'De Lunes a Martes de 2:00 p.m. a 3:00 p.m.', '180', 'Si'),
(28, 'Clase de violin', 'Carlos', 'De Lunes a Martes de 2:00 p.m. a 3:00 p.m.', '120', 'No');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comenta`
--

CREATE TABLE `comenta` (
  `id` int(11) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `comentarios` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `comenta`
--

INSERT INTO `comenta` (`id`, `correo`, `comentarios`) VALUES
(9, 'angelica21sdbf@gmail.com', 'Me encanta 😍'),
(10, 'angelmochi777@gmail.com', 'Amo todoooo'),
(11, 'juanitoalcachofa@gmail.com', 'Excelente página saludos :D'),
(12, 'sanchesitosito@gmail.com', 'Me gustaria comprar el album BE de bts :D');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `idproducto` int(11) NOT NULL,
  `nomproducto` varchar(45) NOT NULL,
  `folio` varchar(45) NOT NULL,
  `caracteristicas` varchar(45) NOT NULL,
  `nomprovedor` varchar(45) NOT NULL,
  `exportado` varchar(45) NOT NULL,
  `precio` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`idproducto`, `nomproducto`, `folio`, `caracteristicas`, `nomprovedor`, `exportado`, `precio`) VALUES
(1, 'Guitarra', '3202', 'Guitarra eléctrica', 'YAMAHA', 'EUA', '680');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro`
--

CREATE TABLE `registro` (
  `id` int(11) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `contrasena` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `registro`
--

INSERT INTO `registro` (`id`, `correo`, `contrasena`) VALUES
(1, 'mochi131095@gmail.com', 'minmin0001'),
(2, 'namu27@hotmail.com', 'armymylove'),
(3, 'taetaev@gmail.com', 'btspavedtheway123'),
(4, 'jungkookie01@hotmail.com', 'jkstrong'),
(5, 'Yurikook123@gmail.com', 'elyu010203'),
(7, 'jose123@hotmail.com', 'bochito86'),
(8, 'yuriflores@hotmail.com', '7628g6y'),
(9, '7turt@gmail.com', 'wqrygqrey');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clases`
--
ALTER TABLE `clases`
  ADD PRIMARY KEY (`idclase`);

--
-- Indices de la tabla `comenta`
--
ALTER TABLE `comenta`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`idproducto`);

--
-- Indices de la tabla `registro`
--
ALTER TABLE `registro`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clases`
--
ALTER TABLE `clases`
  MODIFY `idclase` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de la tabla `comenta`
--
ALTER TABLE `comenta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `idproducto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `registro`
--
ALTER TABLE `registro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
