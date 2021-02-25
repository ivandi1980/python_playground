import psycopg2

con = psycopg2.connect(host="husseinmac",
                        database="husseindb",
                        user="postgres",
                        password = "postgres")

cur = con.cursor()

for i in range(1000000):
    cur.execute("insert into employees (id, name) values(%s,%s) ", (i, f"test{i}"))

#commit 
con.commit()

#close
con.close()
