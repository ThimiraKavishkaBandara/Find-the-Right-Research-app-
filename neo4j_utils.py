from neo4j import GraphDatabase
# Define the Neo4j connection
driver = GraphDatabase.driver("bolt://127.0.0.1:7687", auth=("neo4j", "12345678"), encrypted=False, database="academicworld")

# Define a function to execute the query
def widget_1_query(input):
    with driver.session() as session:
        results = session.run(f"""
            MATCH (K:KEYWORD)<-[INTERESTED_IN]-(uiuc:FACULTY)-[:AFFILIATION_WITH]->(uiuc_inst:INSTITUTE {{name: '{input}' }})
            RETURN K.name, count(*) AS count
            ORDER BY count DESC
            LIMIT 10
        """)
        return [record for record in results]

