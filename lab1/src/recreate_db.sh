#!/bin/sh

user_flag=''
database_flag=''
host_flag=''
user='drukhary'
database='ifmo'
workingDir='.'
host='pg'

print_usage() {
    printf "Usage: ..."
}

while getopts 'U:d:D:h:' flag; do
    case "${flag}" in
    U)
        user_flag='true'
        user="${OPTARG}"
        ;;
    d)
        database_flag='true'
        database="${OPTARG}"
        ;;
    D)
        workingDir="${OPTARG}"
        ;;
    h)
        host_flag='true'
        host="${OPTARG}"
        ;;
    *)
        print_usage
        exit 1
        ;;
    esac
done

"${workingDir}"/src/generate_random_data.py >"${workingDir}"/sqls/insert_data.sql 2>"${workingDir}"/logs/generate_random_data_errors.log

if [ -d "${workingDir}"/logs ]; then
    rm -rf "${workingDir}"/logs
fi

mkdir "${workingDir}"/logs
mkdir "${workingDir}"/logs/errors

psqlOpt=''

if [ "${user_flag}" = 'true' ]; then
    psqlOpt="${psqlOpt} -U ${user}"
fi

if [ "${database_flag}" = 'true' ]; then
    psqlOpt="${psqlOpt} -d ${database}"
fi

if [ "${host_flag}" = 'true' ]; then
    psqlOpt="${psqlOpt} -h ${host}"
fi

psql ${psqlOpt} -a -f "${workingDir}"/sqls/destroy_database.sql >"${workingDir}"/logs/drop.log 2>"${workingDir}"/logs/errors/drop_errors.log
psql ${psqlOpt} -a -f "${workingDir}"/sqls/create_database.sql >"${workingDir}"/logs/init.log 2>"${workingDir}"/logs/errors/init_errors.log
psql ${psqlOpt} -a -f "${workingDir}"/sqls/insert_data.sql >"${workingDir}"/logs/insert.log 2>"${workingDir}"/logs/errors/insert_errors.log