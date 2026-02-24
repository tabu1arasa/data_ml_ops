-include .env
export

deps.lock:
	@uv lock --upgrade

dev.install:
	@uv sync --locked

db.migrate:
	@python3 -m yoyo apply --database ${DB_URL} -b ./migrations

db.rollback:
	@python3 -m yoyo rollback --database ${DB_URL} -b ./migrations

db.migration.new:
	@python3 -m yoyo new --database ${DB_URL} ./migrations -m "${name}"

db.connect:
	@psql ${DB_URL}
