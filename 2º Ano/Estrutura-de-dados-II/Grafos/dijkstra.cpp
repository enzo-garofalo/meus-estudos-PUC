#include <iostream>
#include "list"
#include "dijkstra.h"
#include <bits/stdc++.h>

typedef std::pair<int, int> iPair; 

Graph::Graph(int V)
{
    this->numOfVertices = V;
    adj = new std::list<iPair>[V];
}

void Graph::addEdge(int u, int v, int w)
{
    adj[u].push_back(std::make_pair(v,w));
    adj[v].push_back(std::make_pair(u,w));
}

void Graph::shortestPath(int src)
{
    std::priority_queue<iPair, std::vector<iPair>, std::greater<iPair>> pq;

    std::vector<int> dist(this->numOfVertices, INFINITY);

    pq.push(std::make_pair(0, src));
    dist[src] = 0;

    while(!pq.empty())
    {
        int u = pq.top().second;
        pq.pop();

        std::list<std::pair<int, int>>::iterator i;
        for(i = adj[u].begin(); i != adj[u].end(); i++)
        {
            int v = (*i).first;
            int weight = (*i).second;

            if(dist[v] > dist[u] + weight)
            {
                dist[v] = dist[u] + weight;
                pq.push(std::make_pair(dist[v], v));
            }
        }
    }
    printf("Vertex Distance from Source\n");
    for (int i = 0; i < this->numOfVertices; ++i)
        printf("%d \t\t %d\n", i, dist[i]);
}