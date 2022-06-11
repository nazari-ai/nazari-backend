-- upgrade --
ALTER TABLE "redditCommentTable" DROP CONSTRAINT "fk_redditCo_redditPo_68600dcb";
ALTER TABLE "githubTable" RENAME COLUMN "last_date" TO "last_push_date";
ALTER TABLE "redditCommentTable" ADD "post_id" VARCHAR(255) NOT NULL;
ALTER TABLE "redditCommentTable" DROP COLUMN "post_id_id";
ALTER TABLE "twitterTable" ADD "month" INT NOT NULL;
ALTER TABLE "twitterTable" ADD "hour" INT NOT NULL;
ALTER TABLE "twitterTable" ADD "dow" INT NOT NULL;
ALTER TABLE "redditCommentTable" ADD CONSTRAINT "fk_redditCo_redditPo_cae40ccc" FOREIGN KEY ("post_id") REFERENCES "redditPostTable" ("post_id") ON DELETE CASCADE;
-- downgrade --
ALTER TABLE "redditCommentTable" DROP CONSTRAINT "fk_redditCo_redditPo_cae40ccc";
ALTER TABLE "githubTable" RENAME COLUMN "last_push_date" TO "last_date";
ALTER TABLE "twitterTable" DROP COLUMN "month";
ALTER TABLE "twitterTable" DROP COLUMN "hour";
ALTER TABLE "twitterTable" DROP COLUMN "dow";
ALTER TABLE "redditCommentTable" ADD "post_id_id" VARCHAR(10) NOT NULL;
ALTER TABLE "redditCommentTable" DROP COLUMN "post_id";
ALTER TABLE "redditCommentTable" ADD CONSTRAINT "fk_redditCo_redditPo_68600dcb" FOREIGN KEY ("post_id_id") REFERENCES "redditPostTable" ("post_id") ON DELETE CASCADE;
