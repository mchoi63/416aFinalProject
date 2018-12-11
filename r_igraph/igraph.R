##### Install igraph package #####
#install.packages("igraph")
library("igraph")

##### Read in the data from csv #####
data <- read.csv("CSE-New-Data.csv", header=TRUE, sep=",")

##### Data wrangling #####
# Make the data into a data frame
df <- data.frame(data)

# Change each of the data entries into "character" type
df[] <- lapply(df, as.character)

# Create an edge_list list
edge_list <- list()

# Take the Start area -> dining area from the data frame
edges <- paste(df$Start.Area, df$Dining.Hall, sep=",", collapse=",")

# Put it into an edge list with splitting delimiter ","
edge_list <- strsplit(edges, ",")[[1]]

##### Community Detection and Graphing #####

### 1. Normal, directed graph
# Create a directed graph
g <- make_graph(edges=edge_list, directed=TRUE)

# Add edge attributes (year, school)
E(g)$year <- df$Year
E(g)$school <- df$School

# Plot the graph
plot(g, layout=layout.fruchterman.reingold.grid(g), ylim=c(-0.6,0.8), xlim=c(-1,1), asp=0)

### 2. Modularity maximazation
# Get communities based on modularity maximization
oc <- cluster_optimal(g)

# Add color on the nodes
V(g)$color <- oc$membership + 1

# Add graph layout
g <- set_graph_attr(g, "layout", layout.fruchterman.reingold.grid(g))

# Plot the graph
plot(g, ylim=c(-0.6,0.8), xlim=c(-1,1), asp=0)

### 3. Betweenness-based Clustering
# Make this graph an undirected graph so that we can use edge betweenness
ug <- make_graph(edges=edge_list, directed=FALSE)

# Get communities based on edge betweenness clustering
eb <- cluster_edge_betweenness(ug)

# Add color on the nodes
V(ug)$color <- eb$membership + 1

# Add graph layout
ug <- set_graph_attr(ug, "layout", layout.fruchterman.reingold.grid(ug))

# Plot the graph
plot(ug, rescale=FALSE, ylim=c(-0.3,1.5), xlim=c(-1.7,0.3), asp=0)
