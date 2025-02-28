<template>
  <div class="graph-host"></div>
</template>

<script>
export default {
  data() {
    return {
      value: false,
      ogma: null,
    };
  },
  methods: {
    ErdosRenyi(n = 30, p = 0.2) {
      const graph = { nodes: [], edges: [] };
      let i, j;
      for (i = 0; i < n; i++) {
        graph.nodes.push({ id: i });
        for (j = 0; j < i; j++) {
          if (Math.random() < p) {
            graph.edges.push({ source: i, target: j });
          }
        }
      }
      return graph;
    },
    async layout() {
      return this.ogma.layouts.force({
        autoStop: true,
        edgeLength: 50,
        // alignSiblings: true,
        // charge: 2,
        // gravity: 0.03
      });
    },
    create_ogma() {
      const hostDiv = document.getElementsByClassName("graph-host")[0];
      this.ogma = new Ogma({
        container: hostDiv,
        renderer: "svg",
        options: { backgroundColor: "transparent" },
        interactions: {
          pan: {
            enabled: false,
          },
        },
      });
    },
  },
  async mounted() {
    this.create_ogma();
    const g = this.ErdosRenyi();
    await this.ogma.setGraph(g);
    await this.layout();
    this.ogma.view.locateGraph();
  },
};
</script>

<style>
.graph-host {
  background-color: #c6d0dc;
  padding: 10px;
  width: calc(100vw - 30px);
  height: calc(100vh - 30px);
  border: 1px solid rgb(64, 73, 103);
  border-radius: 4px;
}
</style>
