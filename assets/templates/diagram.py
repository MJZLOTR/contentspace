from diagrams import Diagram, Cluster
from diagrams.opentelekomcloud.computing import Ecs
from diagrams.opentelekomcloud.database import Rds
from diagrams.opentelekomcloud.network import Elb, Dns, Eip

with Diagram("Basic Web App", show=False):
    dns = Dns("dns")
    eip = Eip("eip")

    dns >> eip

    with Cluster("vpc"):
        elb = Elb("dns")

        with Cluster("app-subnet"):
            app = [Ecs("app1"),
            Ecs("app2")]

        with Cluster("db-subnet"):
            db_primary = Rds("primary")
            db_primary - [Rds("replica1"),
                        Rds("replica2")]

    eip >> elb >> app >> db_primary
    