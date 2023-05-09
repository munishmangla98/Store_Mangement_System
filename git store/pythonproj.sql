-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 31, 2023 at 12:15 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pythonproj`
--

-- --------------------------------------------------------

--
-- Table structure for table `allotup`
--

CREATE TABLE `allotup` (
  `sno` int(50) NOT NULL,
  `date` datetime NOT NULL,
  `username` text NOT NULL,
  `proname` text NOT NULL,
  `id_no` text NOT NULL,
  `no_pro` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `allotup`
--

INSERT INTO `allotup` (`sno`, `date`, `username`, `proname`, `id_no`, `no_pro`) VALUES
(1, '2022-12-30 08:20:13', 'Dr.Ranbir Singh', 'Laptop', '', '2'),
(4, '2022-12-30 12:52:48', 'Dr. Hardeep Singh', 'Monitor', '', '3'),
(21, '2023-01-01 15:01:46', 'dr.mohit', 'router', '5', '3'),
(27, '2023-01-05 21:57:45', 'Dr. Harsh', 'Routers', '', ''),
(28, '2023-01-05 22:01:17', '', '', '', ''),
(29, '2023-01-05 22:02:25', 'harry', 'routers', '', ''),
(40, '2023-01-08 22:38:40', '', '', '', ''),
(41, '2023-01-08 22:38:58', 'SAHIL', 'TABLE', '2', '5'),
(43, '2023-01-25 14:22:41', 'rohit', 'routers', '', ''),
(44, '2023-01-25 14:28:25', '', '', '', ''),
(46, '2023-01-25 14:31:13', 'lab', 'computer', '2', '4'),
(47, '2023-01-25 14:31:16', '', '', '', ''),
(48, '2023-01-27 14:31:47', 'mohit', 'chair', '55', '3'),
(49, '2023-01-27 15:32:10', '', '', '', ''),
(50, '2023-01-27 15:32:14', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `enq`
--

CREATE TABLE `enq` (
  `sno` int(50) NOT NULL,
  `date` datetime NOT NULL,
  `username` text NOT NULL,
  `id_no` varchar(50) NOT NULL,
  `email` text NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `enquiry` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `enq`
--

INSERT INTO `enq` (`sno`, `date`, `username`, `id_no`, `email`, `phone_num`, `enquiry`) VALUES
(1, '2022-12-29 19:58:48', 'harry', '1', 'maji@gmail.com', '5533446688', 'is routers avaliable'),
(9, '2022-12-30 11:57:51', 'munish9998', '55', 'munishmangla98@gmail.com', '2233556688', 'chair'),
(20, '2023-01-08 11:19:05', '', '', '', '', ''),
(21, '2023-01-08 22:16:37', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `proup`
--

CREATE TABLE `proup` (
  `sno` int(50) NOT NULL,
  `date` datetime NOT NULL,
  `proname` text NOT NULL,
  `no_pro` text NOT NULL,
  `proid` text NOT NULL,
  `proct` text NOT NULL,
  `delivered` text NOT NULL,
  `remaining` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `proup`
--

INSERT INTO `proup` (`sno`, `date`, `proname`, `no_pro`, `proid`, `proct`, `delivered`, `remaining`) VALUES
(9, '2022-12-30 17:51:48', 'coputer', '5', '5', 'electronic', 'no', '5'),
(17, '2022-12-31 15:14:17', 'chair', '5', '4', 'Furniture', 'no', '5'),
(30, '2022-12-31 20:03:19', 'chair', '5', '4', 'furniture', 'no', '5'),
(35, '2022-12-31 20:05:07', 'chair', '5', '5', 'furniture', 'no', '5'),
(239, '2023-01-03 12:44:24', 'Monitors', '10', '7', 'abc', '2', '8'),
(244, '2023-01-07 23:57:01', 'chair', '10', '5', 'furniture', '2', '8'),
(246, '2023-01-08 11:19:01', 'cha', '2', '5', 'furnituhh', '0', '2'),
(247, '2023-01-08 22:12:34', '', '', '2', 'ele', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `team`
--

CREATE TABLE `team` (
  `sno` int(50) NOT NULL,
  `name` text NOT NULL,
  `date` datetime NOT NULL,
  `dob` date NOT NULL,
  `email` text NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `gender` text NOT NULL,
  `occupation` text NOT NULL,
  `id_type` varchar(50) NOT NULL,
  `id_no` varchar(50) NOT NULL,
  `authority` text NOT NULL,
  `join_status` varchar(50) NOT NULL,
  `doj` date NOT NULL,
  `address` text NOT NULL,
  `nationality` text NOT NULL,
  `state` text NOT NULL,
  `district` text NOT NULL,
  `block_no` varchar(50) NOT NULL,
  `ward_no` varchar(50) NOT NULL,
  `pincode` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `team`
--

INSERT INTO `team` (`sno`, `name`, `date`, `dob`, `email`, `phone_num`, `gender`, `occupation`, `id_type`, `id_no`, `authority`, `join_status`, `doj`, `address`, `nationality`, `state`, `district`, `block_no`, `ward_no`, `pincode`) VALUES
(1, 'Munish', '2022-12-26 15:36:06', '1998-09-01', 'munishmangla98@98gmail.com', '9877674603', 'Male', 'student', 'student', '2', 'Professor', 'Present', '2022-10-01', 'SHAHEED BHAGAT SINGH COLONY, HIRA MAHAL, HOUSE NO.335/3, STREET NO.4, NABHA, PATIALA', 'indian', 'Punjab', 'patiala', '2', '5', '147201'),
(6, 'Horsh', '2023-01-05 15:49:28', '1998-02-05', 'harsh@gmail.com', '5533449988', 'Male', 'Professor', '5', '32', 'Professor', 'present', '2023-01-05', 'banud', 'indian', 'Punjab', 'rajpura', '5', '2', '147002');

-- --------------------------------------------------------

--
-- Table structure for table `teamallot`
--

CREATE TABLE `teamallot` (
  `sno` int(50) NOT NULL,
  `date` datetime NOT NULL,
  `name` text NOT NULL,
  `authority` text NOT NULL,
  `idno` text NOT NULL,
  `idtype` text NOT NULL,
  `proname` text NOT NULL,
  `proct` text NOT NULL,
  `prono` text NOT NULL,
  `delvdate` date NOT NULL,
  `remreq` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `teamallot`
--

INSERT INTO `teamallot` (`sno`, `date`, `name`, `authority`, `idno`, `idtype`, `proname`, `proct`, `prono`, `delvdate`, `remreq`) VALUES
(3, '2022-12-30 19:17:47', 'Munish Mangla', 'cs', '2', 'student', '', 'electronic', '1', '2022-12-30', '0'),
(4, '2022-12-30 21:19:00', '', '', '', '', '', '', '', '0000-00-00', ''),
(5, '2022-12-31 10:36:00', '', '', '', '', '', '', '', '0000-00-00', ''),
(6, '2023-01-01 12:25:07', '', '', '', '', '', '', '', '0000-00-00', ''),
(7, '2023-01-01 12:25:30', '', '', '', '', '', '', '', '0000-00-00', ''),
(8, '2023-01-01 12:25:40', '', '', '', '', '', '', '', '0000-00-00', ''),
(9, '2023-01-01 12:25:51', '', '', '', '', '', '', '', '0000-00-00', ''),
(10, '2023-01-01 12:26:33', '', '', '', '', '', '', '', '0000-00-00', ''),
(11, '2023-01-01 12:38:53', '', '', '', '', '', '', '', '0000-00-00', ''),
(12, '2023-01-01 12:51:31', '', '', '', '', '', '', '', '0000-00-00', ''),
(13, '2023-01-01 13:36:36', '', '', '', '', '', '', '', '0000-00-00', ''),
(14, '2023-01-01 15:46:49', '', '', '', '', '', '', '', '0000-00-00', ''),
(15, '2023-01-02 18:26:47', '', '', '', '', '', '', '', '0000-00-00', ''),
(16, '2023-01-02 18:30:23', '', '', '', '', '', '', '', '0000-00-00', ''),
(17, '2023-01-02 18:33:04', '', '', '', '', '', '', '', '0000-00-00', ''),
(18, '2023-01-05 21:57:42', '', '', '', '', '', '', '', '0000-00-00', ''),
(19, '2023-01-05 22:00:04', '', '', '', '', '', '', '', '0000-00-00', ''),
(20, '2023-01-05 22:03:24', '', '', '', '', '', '', '', '0000-00-00', ''),
(21, '2023-01-05 22:08:16', '', '', '', '', '', '', '', '0000-00-00', ''),
(22, '2023-01-05 22:39:42', '', '', '', '', '', '', '', '0000-00-00', ''),
(23, '2023-01-06 09:53:19', '', '', '', '', '', '', '', '0000-00-00', ''),
(24, '2023-01-06 09:53:48', '', '', '', '', '', '', '', '0000-00-00', ''),
(25, '2023-01-07 23:58:50', '', '', '', '', '', '', '', '0000-00-00', ''),
(26, '2023-01-08 11:19:09', '', '', '', '', '', '', '', '0000-00-00', ''),
(27, '2023-01-08 22:25:14', '', '', '', '', '', '', '', '0000-00-00', ''),
(28, '2023-01-08 22:30:50', '', '', '', '', '', '', '', '0000-00-00', ''),
(29, '2023-01-08 22:30:59', '', '', '', '', '', '', '', '0000-00-00', ''),
(30, '2023-01-08 22:38:37', '', '', '', '', '', '', '', '0000-00-00', ''),
(31, '2023-01-25 14:22:46', '', '', '', '', '', '', '', '0000-00-00', ''),
(32, '2023-01-25 14:27:34', '', '', '', '', '', '', '', '0000-00-00', ''),
(33, '2023-01-27 14:31:55', '', '', '', '', '', '', '', '0000-00-00', '');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `username` text NOT NULL,
  `password` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `email`, `username`, `password`) VALUES
(1, 'munish@gmail.com', 'munish_9', '7894');

-- --------------------------------------------------------

--
-- Table structure for table `ven`
--

CREATE TABLE `ven` (
  `sno` int(50) NOT NULL,
  `date` datetime NOT NULL,
  `proname` varchar(50) NOT NULL,
  `dop` date NOT NULL,
  `billno` varchar(50) NOT NULL,
  `gst` varchar(50) NOT NULL,
  `catogery` text NOT NULL,
  `vender_id` varchar(50) NOT NULL,
  `id_type` varchar(50) NOT NULL,
  `id_no` varchar(50) NOT NULL,
  `authority` text NOT NULL,
  `venstatus` varchar(50) NOT NULL,
  `prorecived` text NOT NULL,
  `address` text NOT NULL,
  `nationality` text NOT NULL,
  `state` text NOT NULL,
  `district` text NOT NULL,
  `shop_no` varchar(50) NOT NULL,
  `ward_no` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `pincode` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ven`
--

INSERT INTO `ven` (`sno`, `date`, `proname`, `dop`, `billno`, `gst`, `catogery`, `vender_id`, `id_type`, `id_no`, `authority`, `venstatus`, `prorecived`, `address`, `nationality`, `state`, `district`, `shop_no`, `ward_no`, `email`, `phone_num`, `pincode`) VALUES
(1, '2022-12-27 10:21:59', 'comptech', '2022-12-01', '45', '456321', 'electronics ', '46', 'electronics', '2', 'research lab', 'left', '2023-01-05', 'patiala', 'indian', 'punjab', '44', '2', '2', 'firstpost@gmail.com', '778866552', '140071'),
(6, '2023-01-05 15:51:06', 'BGIE', '2023-01-05', '44', '22', 'furniture', '2', 'maintenance', '6', 'rearch lab', 'present', '2023-01-05', 'SHAHEED BHAGAT SINGH COLONY', 'indian', 'Punjab', 'hamirpur', '4', '5', 'bgiet@gmail.com', '2233776651', '140021'),
(7, '2023-01-07 23:55:37', 'ram company', '2022-12-07', '55', '04426', 'Electronic', '77', 'Temp', '2', 'Coputer scienc', 'Present', '2023-01-09', 'Patiala', 'Indian', 'Punjab', 'Patiala', '5', '1', 'shop@gmail.com', '8866443322', '1472001');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `allotup`
--
ALTER TABLE `allotup`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `enq`
--
ALTER TABLE `enq`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `proup`
--
ALTER TABLE `proup`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `team`
--
ALTER TABLE `team`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `teamallot`
--
ALTER TABLE `teamallot`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ven`
--
ALTER TABLE `ven`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `allotup`
--
ALTER TABLE `allotup`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `enq`
--
ALTER TABLE `enq`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `proup`
--
ALTER TABLE `proup`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=248;

--
-- AUTO_INCREMENT for table `team`
--
ALTER TABLE `team`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `teamallot`
--
ALTER TABLE `teamallot`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `ven`
--
ALTER TABLE `ven`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
