from diagrams import Diagram
from diagrams.generic.network import Subnet, Switch
from diagrams.onprem.database import PostgreSQL
from diagrams.gcp.network import LoadBalancing

graph_attr = {
        "landscape": "true"
        }

with Diagram("Déploiement de l'opérateur PostgreSQL", show=False, graph_attr = graph_attr ):
    sw = Switch("HAProxy")
    pgbouncer_prim = LoadBalancing("pgBouncer PRIMARY")
    pgbouncer_repl1 = LoadBalancing("pgBouncer STANDBY1")
    pgbouncer_repl2 = LoadBalancing("pgBouncer STANDBY2")
    pgbouncer_repl3 = LoadBalancing("pgBouncer STANDBY3")
    Subnet("") >> sw
    sw >> pgbouncer_prim >> PostgreSQL("write/read")
    sw >> pgbouncer_repl1 >> PostgreSQL("read")
    sw >> pgbouncer_repl2 >> PostgreSQL("read")
    sw >> pgbouncer_repl3 >> PostgreSQL("read")
