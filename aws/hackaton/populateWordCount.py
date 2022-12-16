import boto3, psycopg2

client = boto3.client('rds')

def connection_maker():
    try:
        ENDPOINT = "customer-action-instance-1.cckwth4nvpri.us-west-2.rds.amazonaws.com"
        PORT = 5432
        USR = "postgres"
        REGION = "us-west-2"
        DBNAME = "postgres"
        PASS= "postgres"

        # gets the credentials from .aws/credentials
        session = boto3.Session(profile_name='default',REGION=REGION)
        client = session.client('rds')
        print(f'Client: {client}')

        try:
            conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password=PASS)
            cur = conn.cursor()
            cur.execute("""SELECT 'COMPANY',  'ARTICLES_BLOB' FROM public."customer_Insight";""")
            query_results = cur.fetchall()
            print(f'Query results: {query_results}')
        except Exception as e:
            print("Database connection failed due to {}".format(e))

        return None
    except Exception as error:
        print.error(f'in Creating connection ! {error}')


connection_maker()