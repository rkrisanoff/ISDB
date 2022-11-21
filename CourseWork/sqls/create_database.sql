CREATE TABLE "Robot" (
  "id" serial PRIMARY KEY,
  "brain_series" integer,
  "operator_id" integer,
  "body_series" integer,
  "eye_series" integer,
  "hit_points" integer,
  "asteroid_id" integer
);

CREATE TABLE "positronic_brain" (
  "release_series" serial,
  "name" varchar(255) NOT NULL,
  "speed" int NOT NULL,
  "cost" int NOT NULL
);

CREATE TABLE "body" (
  "release_series" serial,
  "name" varchar(255),
  "max_hit_points" integer,
  "cost" int NOT NULL
);

CREATE TABLE "eyes_sensors" (
  "release_series" serial,
  "name" varchar(255),
  "distance" int,
  "cost" int NOT NULL
);

CREATE TABLE "task" (
  "id" serial,
  "description" varchar(1023),
  "state" varchar(255),
  "creator_post_id" integer,
  "executor_post_id" integer,
  "cost" integer NOT NULL
);

CREATE TABLE "role" (
  "id" serial,
  "name" varchar(255) NOT NULL,
  "salary" int NOT NULL,
  "can_operate_robot" boolean NOT NULL
);

CREATE TABLE "employee" (
  "id" serial,
  "name" varchar(255),
  "age" integer,
  "gender" varchar(6)
);

CREATE TABLE "asteroid" (
  "id" serial,
  "name" varchar(255),
  "distance" integer
);

CREATE TABLE "deposit" (
  "id" serial,
  "asteroid_id" integer,
  "bor_quantity" integer NOT NULL
);

CREATE TABLE "microreactor_type" (
  "id" serial,
  "name" varchar(255) NOT NULL,
  "b2_h6_consumption_rate" integer NOT NULL,
  "b5_h12_consumption_rate" integer NOT NULL,
  "b10_h14_consumption_rate" integer NOT NULL,
  "b12_h12_consumption_rate" integer NOT NULL,
  "cost" integer NOT NULL
);

CREATE TABLE "microreactor_in_spaceship" (
  "microreactor_type_id" integer NOT NULL,
  "spaceship_id" integer NOT NULL,
  "deploy_date" date
);

CREATE TABLE "spaceship" (
  "id" serial,
  "b2_h6_quantity" integer NOT NULL,
  "b5_h12_quantity" integer NOT NULL,
  "b10_h14_quantity" integer NOT NULL,
  "b12_h12_quantity" integer NOT NULL,
  "department_id" integer NOT NULL,
  "income" integer NOT NULL
);

CREATE TABLE "post" (
  "id" serial,
  "employee_id" integer,
  "role_id" integer,
  "department_id" integer,
  "premium" integer NOT NULL
);

CREATE TABLE "department" (
  "id" serial,
  "extracted_bor_quantity" integer NOT NULL,
  "current_resource" integer NOT NULL
);

ALTER TABLE "Robot" ADD FOREIGN KEY ("brain_series") REFERENCES "positronic_brain" ("release_series");

ALTER TABLE "Robot" ADD FOREIGN KEY ("operator_id") REFERENCES "employee" ("id");

ALTER TABLE "Robot" ADD FOREIGN KEY ("body_series") REFERENCES "body" ("release_series");

ALTER TABLE "Robot" ADD FOREIGN KEY ("eye_series") REFERENCES "eyes_sensors" ("release_series");

ALTER TABLE "Robot" ADD FOREIGN KEY ("asteroid_id") REFERENCES "asteroid" ("id");

ALTER TABLE "task" ADD FOREIGN KEY ("creator_post_id") REFERENCES "post" ("id");

ALTER TABLE "task" ADD FOREIGN KEY ("executor_post_id") REFERENCES "post" ("id");

ALTER TABLE "deposit" ADD FOREIGN KEY ("asteroid_id") REFERENCES "asteroid" ("id");

ALTER TABLE "microreactor_in_spaceship" ADD FOREIGN KEY ("microreactor_type_id") REFERENCES "microreactor_type" ("id");

ALTER TABLE "microreactor_in_spaceship" ADD FOREIGN KEY ("spaceship_id") REFERENCES "spaceship" ("id");

ALTER TABLE "spaceship" ADD FOREIGN KEY ("department_id") REFERENCES "department" ("id");

ALTER TABLE "post" ADD FOREIGN KEY ("employee_id") REFERENCES "employee" ("id");

ALTER TABLE "post" ADD FOREIGN KEY ("role_id") REFERENCES "role" ("id");

ALTER TABLE "post" ADD FOREIGN KEY ("department_id") REFERENCES "department" ("id");
