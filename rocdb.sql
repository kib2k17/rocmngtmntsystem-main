/*
 Navicat Premium Dump SQL

 Source Server         : roc_connect
 Source Server Type    : MySQL
 Source Server Version : 80041 (8.0.41)
 Source Host           : localhost:3306
 Source Schema         : rocdb

 Target Server Type    : MySQL
 Target Server Version : 80041 (8.0.41)
 File Encoding         : 65001

 Date: 02/04/2025 20:46:48
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id` ASC, `codename` ASC) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 77 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO `auth_permission` VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO `auth_permission` VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO `auth_permission` VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO `auth_permission` VALUES (21, 'Can add category', 6, 'add_category');
INSERT INTO `auth_permission` VALUES (22, 'Can change category', 6, 'change_category');
INSERT INTO `auth_permission` VALUES (23, 'Can delete category', 6, 'delete_category');
INSERT INTO `auth_permission` VALUES (24, 'Can view category', 6, 'view_category');
INSERT INTO `auth_permission` VALUES (25, 'Can add categorycitymup', 7, 'add_categorycitymup');
INSERT INTO `auth_permission` VALUES (26, 'Can change categorycitymup', 7, 'change_categorycitymup');
INSERT INTO `auth_permission` VALUES (27, 'Can delete categorycitymup', 7, 'delete_categorycitymup');
INSERT INTO `auth_permission` VALUES (28, 'Can view categorycitymup', 7, 'view_categorycitymup');
INSERT INTO `auth_permission` VALUES (29, 'Can add state', 8, 'add_state');
INSERT INTO `auth_permission` VALUES (30, 'Can change state', 8, 'change_state');
INSERT INTO `auth_permission` VALUES (31, 'Can delete state', 8, 'delete_state');
INSERT INTO `auth_permission` VALUES (32, 'Can view state', 8, 'view_state');
INSERT INTO `auth_permission` VALUES (33, 'Can add user', 9, 'add_customuser');
INSERT INTO `auth_permission` VALUES (34, 'Can change user', 9, 'change_customuser');
INSERT INTO `auth_permission` VALUES (35, 'Can delete user', 9, 'delete_customuser');
INSERT INTO `auth_permission` VALUES (36, 'Can view user', 9, 'view_customuser');
INSERT INTO `auth_permission` VALUES (37, 'Can add complaints', 10, 'add_complaints');
INSERT INTO `auth_permission` VALUES (38, 'Can change complaints', 10, 'change_complaints');
INSERT INTO `auth_permission` VALUES (39, 'Can delete complaints', 10, 'delete_complaints');
INSERT INTO `auth_permission` VALUES (40, 'Can view complaints', 10, 'view_complaints');
INSERT INTO `auth_permission` VALUES (41, 'Can add complaint remark', 11, 'add_complaintremark');
INSERT INTO `auth_permission` VALUES (42, 'Can change complaint remark', 11, 'change_complaintremark');
INSERT INTO `auth_permission` VALUES (43, 'Can delete complaint remark', 11, 'delete_complaintremark');
INSERT INTO `auth_permission` VALUES (44, 'Can view complaint remark', 11, 'view_complaintremark');
INSERT INTO `auth_permission` VALUES (45, 'Can add subcategory', 12, 'add_subcategory');
INSERT INTO `auth_permission` VALUES (46, 'Can change subcategory', 12, 'change_subcategory');
INSERT INTO `auth_permission` VALUES (47, 'Can delete subcategory', 12, 'delete_subcategory');
INSERT INTO `auth_permission` VALUES (48, 'Can view subcategory', 12, 'view_subcategory');
INSERT INTO `auth_permission` VALUES (49, 'Can add subcategorycitymup', 13, 'add_subcategorycitymup');
INSERT INTO `auth_permission` VALUES (50, 'Can change subcategorycitymup', 13, 'change_subcategorycitymup');
INSERT INTO `auth_permission` VALUES (51, 'Can delete subcategorycitymup', 13, 'delete_subcategorycitymup');
INSERT INTO `auth_permission` VALUES (52, 'Can view subcategorycitymup', 13, 'view_subcategorycitymup');
INSERT INTO `auth_permission` VALUES (53, 'Can add user reg', 14, 'add_userreg');
INSERT INTO `auth_permission` VALUES (54, 'Can change user reg', 14, 'change_userreg');
INSERT INTO `auth_permission` VALUES (55, 'Can delete user reg', 14, 'delete_userreg');
INSERT INTO `auth_permission` VALUES (56, 'Can view user reg', 14, 'view_userreg');
INSERT INTO `auth_permission` VALUES (57, 'Can add pacd complaint remark', 15, 'add_pacdcomplaintremark');
INSERT INTO `auth_permission` VALUES (58, 'Can change pacd complaint remark', 15, 'change_pacdcomplaintremark');
INSERT INTO `auth_permission` VALUES (59, 'Can delete pacd complaint remark', 15, 'delete_pacdcomplaintremark');
INSERT INTO `auth_permission` VALUES (60, 'Can view pacd complaint remark', 15, 'view_pacdcomplaintremark');
INSERT INTO `auth_permission` VALUES (61, 'Can add pacd complaints', 16, 'add_pacdcomplaints');
INSERT INTO `auth_permission` VALUES (62, 'Can change pacd complaints', 16, 'change_pacdcomplaints');
INSERT INTO `auth_permission` VALUES (63, 'Can delete pacd complaints', 16, 'delete_pacdcomplaints');
INSERT INTO `auth_permission` VALUES (64, 'Can view pacd complaints', 16, 'view_pacdcomplaints');
INSERT INTO `auth_permission` VALUES (65, 'Can add odsus', 17, 'add_odsus');
INSERT INTO `auth_permission` VALUES (66, 'Can change odsus', 17, 'change_odsus');
INSERT INTO `auth_permission` VALUES (67, 'Can delete odsus', 17, 'delete_odsus');
INSERT INTO `auth_permission` VALUES (68, 'Can view odsus', 17, 'view_odsus');
INSERT INTO `auth_permission` VALUES (69, 'Can add odsus remark', 18, 'add_odsusremark');
INSERT INTO `auth_permission` VALUES (70, 'Can change odsus remark', 18, 'change_odsusremark');
INSERT INTO `auth_permission` VALUES (71, 'Can delete odsus remark', 18, 'delete_odsusremark');
INSERT INTO `auth_permission` VALUES (72, 'Can view odsus remark', 18, 'view_odsusremark');
INSERT INTO `auth_permission` VALUES (73, 'Can add user activity log', 19, 'add_useractivitylog');
INSERT INTO `auth_permission` VALUES (74, 'Can change user activity log', 19, 'change_useractivitylog');
INSERT INTO `auth_permission` VALUES (75, 'Can delete user activity log', 19, 'delete_useractivitylog');
INSERT INTO `auth_permission` VALUES (76, 'Can view user activity log', 19, 'view_useractivitylog');

-- ----------------------------
-- Table structure for cmsapp_category
-- ----------------------------
DROP TABLE IF EXISTS `cmsapp_category`;
CREATE TABLE `cmsapp_category`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `catname` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `catdes` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cmsapp_category
-- ----------------------------

-- ----------------------------
-- Table structure for cmsapp_categorycitymup
-- ----------------------------
DROP TABLE IF EXISTS `cmsapp_categorycitymup`;
CREATE TABLE `cmsapp_categorycitymup`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `catcitymupname` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `catcitymupdes` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cmsapp_categorycitymup
-- ----------------------------

-- ----------------------------
-- Table structure for cmsapp_complaintremark
-- ----------------------------
DROP TABLE IF EXISTS `cmsapp_complaintremark`;
CREATE TABLE `cmsapp_complaintremark`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `remark` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `remarkdate` datetime(6) NOT NULL,
  `comp_id_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `cmsapp_complaintrema_comp_id_id_id_eef57696_fk_cmsapp_co`(`comp_id_id_id` ASC) USING BTREE,
  CONSTRAINT `cmsapp_complaintrema_comp_id_id_id_eef57696_fk_cmsapp_co` FOREIGN KEY (`comp_id_id_id`) REFERENCES `cmsapp_complaints` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cmsapp_complaintremark
-- ----------------------------

-- ----------------------------
-- Table structure for cmsapp_complaints
-- ----------------------------
DROP TABLE IF EXISTS `cmsapp_complaints`;
CREATE TABLE `cmsapp_complaints`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `deadline` date NULL DEFAULT NULL,
  `passed_date` date NULL DEFAULT NULL,
  `date_received` date NULL DEFAULT NULL,
  `time_received` time(6) NULL DEFAULT NULL,
  `complaint_number` int NOT NULL,
  `selfcomplaint_number` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `complainant_pace` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `complaint_email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `complaint_text` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `complainttype` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `noc` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `complainant_fname` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `complaindetails` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `compfile` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `complaintdate_at` datetime(6) NOT NULL,
  `remark` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `cat_id_id` bigint NOT NULL,
  `subcategory_id_id` bigint NOT NULL,
  `userregid_id` bigint NULL DEFAULT NULL,
  `barangay_name` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `city_name` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `clientdetails` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `date_endorse` date NULL DEFAULT NULL,
  `endorseemp` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `province_name` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `region_name` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `remind_date` date NULL DEFAULT NULL,
  `time_acknowledge` time(6) NULL DEFAULT NULL,
  `time_endorse` time(6) NULL DEFAULT NULL,
  `cog` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `cmsapp_complaints_subcategory_id_id_05376955_fk_cmsapp_su`(`subcategory_id_id` ASC) USING BTREE,
  INDEX `cmsapp_complaints_userregid_id_11f44224_fk_cmsapp_userreg_id`(`userregid_id` ASC) USING BTREE,
  INDEX `cmsapp_complaints_cat_id_id_6c81c042_fk_cmsapp_category_id`(`cat_id_id` ASC) USING BTREE,
  CONSTRAINT `cmsapp_complaints_cat_id_id_6c81c042_fk_cmsapp_category_id` FOREIGN KEY (`cat_id_id`) REFERENCES `cmsapp_category` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `cmsapp_complaints_subcategory_id_id_05376955_fk_cmsapp_su` FOREIGN KEY (`subcategory_id_id`) REFERENCES `cmsapp_subcategory` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `cmsapp_complaints_userregid_id_11f44224_fk_cmsapp_userreg_id` FOREIGN KEY (`userregid_id`) REFERENCES `cmsapp_userreg` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cmsapp_complaints
-- ----------------------------

-- ----------------------------
-- Table structure for cmsapp_customuser
-- ----------------------------
DROP TABLE IF EXISTS `cmsapp_customuser`;
CREATE TABLE `cmsapp_customuser`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `user_type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `profile_pic` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `cat_id` bigint NULL DEFAULT NULL,
  `subcategory_id` bigint NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username` ASC) USING BTREE,
  INDEX `cmsapp_customuser_cat_id_1af26226_fk_cmsapp_category_id`(`cat_id` ASC) USING BTREE,
  INDEX `cmsapp_customuser_subcategory_id_af1df1d8_fk_cmsapp_su`(`subcategory_id` ASC) USING BTREE,
  CONSTRAINT `cmsapp_customuser_cat_id_1af26226_fk_cmsapp_category_id` FOREIGN KEY (`cat_id`) REFERENCES `cmsapp_category` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `cmsapp_customuser_subcategory_id_af1df1d8_fk_cmsapp_su` FOREIGN KEY (`subcategory_id`) REFERENCES `cmsapp_subcategory` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cmsapp_customuser
-- ----------------------------

-- ----------------------------
-- Table structure for cmsapp_customuser_groups
-- ----------------------------
DROP TABLE IF EXISTS `cmsapp_customuser_groups`;
CREATE TABLE `cmsapp_customuser_groups`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `cmsapp_customuser_groups_customuser_id_group_id_45650982_uniq`(`customuser_id` ASC, `group_id` ASC) USING BTREE,
  INDEX `cmsapp_customuser_groups_group_id_9d73370c_fk_auth_group_id`(`group_id` ASC) USING BTREE,
  CONSTRAINT `cmsapp_customuser_gr_customuser_id_63c3707f_fk_cmsapp_cu` FOREIGN KEY (`customuser_id`) REFERENCES `cmsapp_customuser` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `cmsapp_customuser_groups_group_id_9d73370c_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cmsapp_customuser_groups
-- ----------------------------

-- ----------------------------
-- Table structure for cmsapp_customuser_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `cmsapp_customuser_user_permissions`;
CREATE TABLE `cmsapp_customuser_user_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `cmsapp_customuser_user_p_customuser_id_permission_3100a3a5_uniq`(`customuser_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `cmsapp_customuser_us_permission_id_bf407ca8_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `cmsapp_customuser_us_customuser_id_820f4ca8_fk_cmsapp_cu` FOREIGN KEY (`customuser_id`) REFERENCES `cmsapp_customuser` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `cmsapp_customuser_us_permission_id_bf407ca8_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cmsapp_customuser_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for cmsapp_odsus
-- ----------------------------
DROP TABLE IF EXISTS `cmsapp_odsus`;
CREATE TABLE `cmsapp_odsus`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `deadline` date NULL DEFAULT NULL,
  `passed_date` date NULL DEFAULT NULL,
  `date_received` date NULL DEFAULT NULL,
  `date_endorse` date NULL DEFAULT NULL,
  `remind_date` date NULL DEFAULT NULL,
  `time_received` time(6) NULL DEFAULT NULL,
  `time_acknowledge` time(6) NULL DEFAULT NULL,
  `time_endorse` time(6) NULL DEFAULT NULL,
  `region_name` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `province_name` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `city_name` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `barangay_name` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `complaint_number` int NOT NULL,
  `selfcomplaint_number` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `complainant_pace` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `complaint_email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `complaint_text` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `complainttype` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `clientdetails` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `noc` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `endorseemp` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `complainant_fname` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `complaindetails` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `compfile` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `complaintdate_at` datetime(6) NOT NULL,
  `remark` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `cat_id_id` bigint NULL DEFAULT NULL,
  `subcategory_id_id` bigint NULL DEFAULT NULL,
  `userregid_id` bigint NULL DEFAULT NULL,
  `cog` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `cmsapp_odsus_cat_id_id_28e85567_fk_cmsapp_category_id`(`cat_id_id` ASC) USING BTREE,
  INDEX `cmsapp_odsus_subcategory_id_id_f9c0fb78_fk_cmsapp_subcategory_id`(`subcategory_id_id` ASC) USING BTREE,
  INDEX `cmsapp_odsus_userregid_id_165fc1ce_fk_cmsapp_userreg_id`(`userregid_id` ASC) USING BTREE,
  CONSTRAINT `cmsapp_odsus_cat_id_id_28e85567_fk_cmsapp_category_id` FOREIGN KEY (`cat_id_id`) REFERENCES `cmsapp_category` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `cmsapp_odsus_subcategory_id_id_f9c0fb78_fk_cmsapp_subcategory_id` FOREIGN KEY (`subcategory_id_id`) REFERENCES `cmsapp_subcategory` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `cmsapp_odsus_userregid_id_165fc1ce_fk_cmsapp_userreg_id` FOREIGN KEY (`userregid_id`) REFERENCES `cmsapp_userreg` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cmsapp_odsus
-- ----------------------------

-- ----------------------------
-- Table structure for cmsapp_odsus_complaints
-- ----------------------------
DROP TABLE IF EXISTS `cmsapp_odsus_complaints`;
CREATE TABLE `cmsapp_odsus_complaints`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `odsus_id` bigint NOT NULL,
  `complaints_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `cmsapp_odsus_complaints_odsus_id_complaints_id_bdb579c6_uniq`(`odsus_id` ASC, `complaints_id` ASC) USING BTREE,
  INDEX `cmsapp_odsus_complai_complaints_id_ddfe0e95_fk_cmsapp_co`(`complaints_id` ASC) USING BTREE,
  CONSTRAINT `cmsapp_odsus_complai_complaints_id_ddfe0e95_fk_cmsapp_co` FOREIGN KEY (`complaints_id`) REFERENCES `cmsapp_complaints` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `cmsapp_odsus_complaints_odsus_id_a30b9dc6_fk_cmsapp_odsus_id` FOREIGN KEY (`odsus_id`) REFERENCES `cmsapp_odsus` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cmsapp_odsus_complaints
-- ----------------------------

-- ----------------------------
-- Table structure for cmsapp_odsusremark
-- ----------------------------
DROP TABLE IF EXISTS `cmsapp_odsusremark`;
CREATE TABLE `cmsapp_odsusremark`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `remark` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `remarkdate` datetime(6) NOT NULL,
  `comp_id_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `cmsapp_odsusremark_comp_id_id_id_836cd3f4_fk_cmsapp_co`(`comp_id_id_id` ASC) USING BTREE,
  CONSTRAINT `cmsapp_odsusremark_comp_id_id_id_836cd3f4_fk_cmsapp_co` FOREIGN KEY (`comp_id_id_id`) REFERENCES `cmsapp_complaints` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cmsapp_odsusremark
-- ----------------------------

-- ----------------------------
-- Table structure for cmsapp_pacdcomplaintremark
-- ----------------------------
DROP TABLE IF EXISTS `cmsapp_pacdcomplaintremark`;
CREATE TABLE `cmsapp_pacdcomplaintremark`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `remark` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `remarkdate` datetime(6) NOT NULL,
  `comp_id_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `cmsapp_pacdcomplaint_comp_id_id_id_76ad7410_fk_cmsapp_co`(`comp_id_id_id` ASC) USING BTREE,
  CONSTRAINT `cmsapp_pacdcomplaint_comp_id_id_id_76ad7410_fk_cmsapp_co` FOREIGN KEY (`comp_id_id_id`) REFERENCES `cmsapp_complaints` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cmsapp_pacdcomplaintremark
-- ----------------------------

-- ----------------------------
-- Table structure for cmsapp_pacdcomplaints
-- ----------------------------
DROP TABLE IF EXISTS `cmsapp_pacdcomplaints`;
CREATE TABLE `cmsapp_pacdcomplaints`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `deadline` date NULL DEFAULT NULL,
  `passed_date` date NULL DEFAULT NULL,
  `date_received` date NULL DEFAULT NULL,
  `date_endorse` date NULL DEFAULT NULL,
  `remind_date` date NULL DEFAULT NULL,
  `time_received` time(6) NULL DEFAULT NULL,
  `time_acknowledge` time(6) NULL DEFAULT NULL,
  `time_endorse` time(6) NULL DEFAULT NULL,
  `region_name` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `province_name` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `city_name` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `barangay_name` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `complaint_number` int NOT NULL,
  `selfcomplaint_number` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `complainant_pace` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `complaint_email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `complaint_text` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `complainttype` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `clientdetails` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `noc` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `endorseemp` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `complainant_fname` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `complaindetails` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `compfile` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `complaintdate_at` datetime(6) NOT NULL,
  `remark` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `cat_id_id` bigint NULL DEFAULT NULL,
  `subcategory_id_id` bigint NULL DEFAULT NULL,
  `userregid_id` bigint NULL DEFAULT NULL,
  `cog` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `cmsapp_pacdcomplaints_cat_id_id_7ac6ce0c_fk_cmsapp_category_id`(`cat_id_id` ASC) USING BTREE,
  INDEX `cmsapp_pacdcomplaint_subcategory_id_id_2c822397_fk_cmsapp_su`(`subcategory_id_id` ASC) USING BTREE,
  INDEX `cmsapp_pacdcomplaints_userregid_id_e12ca761_fk_cmsapp_userreg_id`(`userregid_id` ASC) USING BTREE,
  CONSTRAINT `cmsapp_pacdcomplaint_subcategory_id_id_2c822397_fk_cmsapp_su` FOREIGN KEY (`subcategory_id_id`) REFERENCES `cmsapp_subcategory` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `cmsapp_pacdcomplaints_cat_id_id_7ac6ce0c_fk_cmsapp_category_id` FOREIGN KEY (`cat_id_id`) REFERENCES `cmsapp_category` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `cmsapp_pacdcomplaints_userregid_id_e12ca761_fk_cmsapp_userreg_id` FOREIGN KEY (`userregid_id`) REFERENCES `cmsapp_userreg` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cmsapp_pacdcomplaints
-- ----------------------------

-- ----------------------------
-- Table structure for cmsapp_state
-- ----------------------------
DROP TABLE IF EXISTS `cmsapp_state`;
CREATE TABLE `cmsapp_state`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `statename` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cmsapp_state
-- ----------------------------

-- ----------------------------
-- Table structure for cmsapp_subcategory
-- ----------------------------
DROP TABLE IF EXISTS `cmsapp_subcategory`;
CREATE TABLE `cmsapp_subcategory`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `subcatname` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `cat_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `cmsapp_subcategory_cat_id_id_996bae74_fk_cmsapp_category_id`(`cat_id_id` ASC) USING BTREE,
  CONSTRAINT `cmsapp_subcategory_cat_id_id_996bae74_fk_cmsapp_category_id` FOREIGN KEY (`cat_id_id`) REFERENCES `cmsapp_category` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cmsapp_subcategory
-- ----------------------------

-- ----------------------------
-- Table structure for cmsapp_subcategorycitymup
-- ----------------------------
DROP TABLE IF EXISTS `cmsapp_subcategorycitymup`;
CREATE TABLE `cmsapp_subcategorycitymup`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `subcatcitymupname` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `catmupname_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `cmsapp_subcategoryci_catmupname_id_id_77a429de_fk_cmsapp_ca`(`catmupname_id_id` ASC) USING BTREE,
  CONSTRAINT `cmsapp_subcategoryci_catmupname_id_id_77a429de_fk_cmsapp_ca` FOREIGN KEY (`catmupname_id_id`) REFERENCES `cmsapp_categorycitymup` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cmsapp_subcategorycitymup
-- ----------------------------

-- ----------------------------
-- Table structure for cmsapp_useractivitylog
-- ----------------------------
DROP TABLE IF EXISTS `cmsapp_useractivitylog`;
CREATE TABLE `cmsapp_useractivitylog`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `action` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `cmsapp_useractivitylog_user_id_9e8921e2_fk_cmsapp_customuser_id`(`user_id` ASC) USING BTREE,
  CONSTRAINT `cmsapp_useractivitylog_user_id_9e8921e2_fk_cmsapp_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `cmsapp_customuser` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cmsapp_useractivitylog
-- ----------------------------

-- ----------------------------
-- Table structure for cmsapp_userreg
-- ----------------------------
DROP TABLE IF EXISTS `cmsapp_userreg`;
CREATE TABLE `cmsapp_userreg`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `mobilenumber` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `regdate_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `admin_id` bigint NULL DEFAULT NULL,
  `cat_id` bigint NULL DEFAULT NULL,
  `subcategory_id` bigint NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `admin_id`(`admin_id` ASC) USING BTREE,
  INDEX `cmsapp_userreg_cat_id_d6e9cddd_fk_cmsapp_category_id`(`cat_id` ASC) USING BTREE,
  INDEX `cmsapp_userreg_subcategory_id_21d9e8c2_fk_cmsapp_subcategory_id`(`subcategory_id` ASC) USING BTREE,
  CONSTRAINT `cmsapp_userreg_admin_id_94e4b9b8_fk_cmsapp_customuser_id` FOREIGN KEY (`admin_id`) REFERENCES `cmsapp_customuser` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `cmsapp_userreg_cat_id_d6e9cddd_fk_cmsapp_category_id` FOREIGN KEY (`cat_id`) REFERENCES `cmsapp_category` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `cmsapp_userreg_subcategory_id_21d9e8c2_fk_cmsapp_subcategory_id` FOREIGN KEY (`subcategory_id`) REFERENCES `cmsapp_subcategory` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cmsapp_userreg
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int NULL DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id` ASC) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_cmsapp_customuser_id`(`user_id` ASC) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_cmsapp_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `cmsapp_customuser` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_chk_1` CHECK (`action_flag` >= 0)
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label` ASC, `model` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (6, 'cmsapp', 'category');
INSERT INTO `django_content_type` VALUES (7, 'cmsapp', 'categorycitymup');
INSERT INTO `django_content_type` VALUES (11, 'cmsapp', 'complaintremark');
INSERT INTO `django_content_type` VALUES (10, 'cmsapp', 'complaints');
INSERT INTO `django_content_type` VALUES (9, 'cmsapp', 'customuser');
INSERT INTO `django_content_type` VALUES (17, 'cmsapp', 'odsus');
INSERT INTO `django_content_type` VALUES (18, 'cmsapp', 'odsusremark');
INSERT INTO `django_content_type` VALUES (15, 'cmsapp', 'pacdcomplaintremark');
INSERT INTO `django_content_type` VALUES (16, 'cmsapp', 'pacdcomplaints');
INSERT INTO `django_content_type` VALUES (8, 'cmsapp', 'state');
INSERT INTO `django_content_type` VALUES (12, 'cmsapp', 'subcategory');
INSERT INTO `django_content_type` VALUES (13, 'cmsapp', 'subcategorycitymup');
INSERT INTO `django_content_type` VALUES (19, 'cmsapp', 'useractivitylog');
INSERT INTO `django_content_type` VALUES (14, 'cmsapp', 'userreg');
INSERT INTO `django_content_type` VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (5, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 36 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2025-04-02 12:36:23.432930');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2025-04-02 12:36:23.499867');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2025-04-02 12:36:23.732964');
INSERT INTO `django_migrations` VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2025-04-02 12:36:23.820700');
INSERT INTO `django_migrations` VALUES (5, 'auth', '0003_alter_user_email_max_length', '2025-04-02 12:36:23.824713');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0004_alter_user_username_opts', '2025-04-02 12:36:23.829712');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0005_alter_user_last_login_null', '2025-04-02 12:36:23.834370');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0006_require_contenttypes_0002', '2025-04-02 12:36:23.836355');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2025-04-02 12:36:23.840374');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0008_alter_user_username_max_length', '2025-04-02 12:36:23.845371');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2025-04-02 12:36:23.849370');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0010_alter_group_name_max_length', '2025-04-02 12:36:23.860570');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0011_update_proxy_permissions', '2025-04-02 12:36:23.865585');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0012_alter_user_first_name_max_length', '2025-04-02 12:36:23.869953');
INSERT INTO `django_migrations` VALUES (15, 'cmsapp', '0001_initial', '2025-04-02 12:36:24.738771');
INSERT INTO `django_migrations` VALUES (16, 'admin', '0001_initial', '2025-04-02 12:36:24.857526');
INSERT INTO `django_migrations` VALUES (17, 'admin', '0002_logentry_remove_auto_add', '2025-04-02 12:36:24.863525');
INSERT INTO `django_migrations` VALUES (18, 'admin', '0003_logentry_add_action_flag_choices', '2025-04-02 12:36:24.869561');
INSERT INTO `django_migrations` VALUES (19, 'cmsapp', '0002_remove_complaints_catmupname_id_and_more', '2025-04-02 12:36:25.850189');
INSERT INTO `django_migrations` VALUES (20, 'cmsapp', '0003_alter_customuser_user_type_odsus_odsusremark', '2025-04-02 12:36:26.082688');
INSERT INTO `django_migrations` VALUES (21, 'cmsapp', '0004_alter_customuser_profile_pic_and_more', '2025-04-02 12:36:26.135509');
INSERT INTO `django_migrations` VALUES (22, 'cmsapp', '0005_userreg_cat_id_userreg_subcategory_id', '2025-04-02 12:36:26.253093');
INSERT INTO `django_migrations` VALUES (23, 'cmsapp', '0006_remove_userreg_cat_id_remove_userreg_subcategory_id_and_more', '2025-04-02 12:36:26.495189');
INSERT INTO `django_migrations` VALUES (24, 'cmsapp', '0007_customuser_cat_customuser_subcategory', '2025-04-02 12:36:26.610837');
INSERT INTO `django_migrations` VALUES (25, 'cmsapp', '0008_odsus_complaint', '2025-04-02 12:36:26.674921');
INSERT INTO `django_migrations` VALUES (26, 'cmsapp', '0009_remove_odsus_complaint_odsus_complaints', '2025-04-02 12:36:26.859665');
INSERT INTO `django_migrations` VALUES (27, 'cmsapp', '0010_complaints_cog_odsus_cog_pacdcomplaints_cog', '2025-04-02 12:36:26.999978');
INSERT INTO `django_migrations` VALUES (28, 'cmsapp', '0011_remove_complaints_cog', '2025-04-02 12:36:27.050813');
INSERT INTO `django_migrations` VALUES (29, 'cmsapp', '0012_complaints_cog', '2025-04-02 12:36:27.102851');
INSERT INTO `django_migrations` VALUES (30, 'cmsapp', '0013_useractivitylog', '2025-04-02 12:36:27.166067');
INSERT INTO `django_migrations` VALUES (31, 'cmsapp', '0014_alter_complaints_updated_at', '2025-04-02 12:36:27.255600');
INSERT INTO `django_migrations` VALUES (32, 'cmsapp', '0015_alter_complaints_updated_at', '2025-04-02 12:36:27.322430');
INSERT INTO `django_migrations` VALUES (33, 'cmsapp', '0016_alter_complaints_date_endorse', '2025-04-02 12:36:27.386808');
INSERT INTO `django_migrations` VALUES (34, 'cmsapp', '0017_alter_complaints_date_endorse', '2025-04-02 12:36:27.452799');
INSERT INTO `django_migrations` VALUES (35, 'sessions', '0001_initial', '2025-04-02 12:36:27.481523');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
