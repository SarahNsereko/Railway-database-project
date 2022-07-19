CREATE TABLE `Passengers` (
  `passenger_id` int PRIMARY KEY AUTO_INCREMENT,
  `passenger_name` text,
  `age` int,
  `bag` int,
  `seats` int,
  `amont` int
);

CREATE TABLE `Train` (
  `train_id` int PRIMARY KEY AUTO_INCREMENT,
  `train_no` int,
  `train_name` text,
  `destination` text,
  `setoff_time` text,
  `arrival_time` text
);

CREATE TABLE `Stations` (
  `station_id` int PRIMARY KEY AUTO_INCREMENT,
  `station_no` int,
  `station_name` text,
  `station_location` text
);

CREATE TABLE `Tickets` (
  `ticket_no` int PRIMARY KEY AUTO_INCREMENT,
  `issue_date` text,
  `passenger_id` int,
  `train_id` int,
  `station_id` int
);

ALTER TABLE `Tickets` ADD FOREIGN KEY (`passenger_id`) REFERENCES `Passengers` (`passenger_id`);

ALTER TABLE `Tickets` ADD FOREIGN KEY (`train_id`) REFERENCES `Train` (`train_id`);

ALTER TABLE `Tickets` ADD FOREIGN KEY (`station_id`) REFERENCES `Stations` (`station_id`);
