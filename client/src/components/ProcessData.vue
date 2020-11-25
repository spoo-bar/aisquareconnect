<template>
  <div id="process-data-form">
    <b-card>
        <b-form>
            <b-form-group
                id="input-file"
            >
                <b-form-file
                v-model="file"
                accept=".csv"
                placeholder="Choose a file or drop it here..."
                drop-placeholder="Drop file here..."
                ></b-form-file>
            </b-form-group>
        </b-form>
        <b-button variant="primary" @click="submit">Submit</b-button>
        <div v-if="error">
          <hr />
            <b-card
              border-variant="danger"
              header="Error"
              header-border-variant="danger"
              header-text-variant="danger"
              align="center"
            >
              <b-card-text>{{this.errorMessage}}</b-card-text>
            </b-card>
          </div>
        <div v-if="processingId !== ''">
          <hr />
          <p v-if="processing">Processing..</p>
          <h2>Processed file : {{this.processedFile}}</h2>
          <b-row>
            <a :href="csvUrl" download="output.csv" style="padding-left:15px;">Download Output</a>
          </b-row>
          <b-row>
            <img :src="imageUrl" />
          </b-row>
        </div>
    </b-card>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import axios from 'axios';

@Component
export default class ProcessData extends Vue {
  private file: File = new File([''], 'filename');

  private processingId ='';

  private imageUrl = '#';

  private csvUrl = '#';

  private processedFile = '';

  private processing = false;

  private error = false;

  private errorMessage = '';

  submit() {
    if (this.file.size) {
      this.error = false;
      this.processing = true;
      const processingUrl = `${this.$store.state.backendUrl}/processing`;
      const formData = new FormData();
      formData.append('process_file', this.file, this.file.name);
      const bearerToken = `Bearer ${this.$store.state.accessToken}`;
      axios.post(processingUrl, formData, {
        headers: { 'Content-Type': 'multipart/form-data', Authorization: bearerToken },
      }).then((response) => {
        console.log(response);
        if (response) {
          this.processingId = response.data.processing_id;
          this.imageUrl = `${this.$store.state.backendUrl}/processing/image/${this.processingId}`;
          this.csvUrl = `${this.$store.state.backendUrl}/processing/csv/${this.processingId}`;
          this.processedFile = this.file.name;
          this.file = null;
          this.processing = false;
        }
      }).catch((error) => {
        this.error = true;
        this.processing = false;
        this.processingId = '';
        this.errorMessage = error.response.data.response;
      });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
