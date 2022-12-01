import React from 'react'
import {Line} from 'react-chartjs-2';
import myData from '../utils/adata.json';

import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    Filler,
  } from 'chart.js';
  
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend,Filler);


//data
const data = {

  labels: myData.map((item)=>{
    return item.year;
  }),
  datasets: [
    //RUG
      {
        label: 'RUG',
        fill: true,
        lineTension: 0.5,
        backgroundColor: 'rgba(75,192,192,1)',
        borderColor: 'rgba(75,192,192,1)',
        borderWidth: 2,
        data: myData.map((item) =>{
          return item.RUG;
        })
      },
    //UvA
      {
        label: 'UvA',
        fill: true,
        lineTension: 0.5,
        backgroundColor: 'rgba(70,130,180,1)',
        borderColor: 'rgba(70,130,180,1)',
        borderWidth: 2,
        data: myData.map((item)=>{
          return item.UvA;
        })
      },
    //RU
      {
        label: 'RU',
        fill: true,
        lineTension: 0.5,
        backgroundColor: 'rgba(85,107,47,1)',
        borderColor: 'rgba(85,107,47,1)',
        borderWidth: 2,
        data: myData.map((item)=>{
          return item.RU;
        })
      },
    //VU
      {
        label: 'VU',
        fill: true,
        lineTension: 0.5,
        backgroundColor: 'rgba(255,0,127,1)',
        borderColor: 'rgba(255,0,127,1)',
        borderWidth: 2,
        data: myData.map((item)=>{
          return item.VU;
        })
      },
    //TUD
      {
        label: 'TUD',
        fill: true,
        lineTension: 0.5,
        backgroundColor: 'rgba(220,20,60,1)',
        borderColor: 'rgba(220,20,60,1)',
        borderWidth: 2,
        data: myData.map((item)=>{
          return item.TUD;
        })
      },
    //TUE
      {
        label: 'TUE',
        fill: true,
        lineTension: 0.5,
        backgroundColor: 'rgba(138,43,226,1)',
        borderColor: 'rgba(138,43,226,1)',
        borderWidth: 2,
        data: myData.map((item)=>{
          return item.TUE;
        })
      },
    //WUR
      {
        label: 'WUR',
        fill: true,
        lineTension: 0.5,
        backgroundColor: 'rgba(0,0,205,1)',
        borderColor: 'rgba(0,0,205,1)',
        borderWidth: 2,
        data: myData.map((item)=>{
          return item.WUR;
        })
      },
    //EUR
      {
        label: 'EUR',
        fill: true,
        lineTension: 0.5,
        backgroundColor: 'rgba(0,128,128,1)',
        borderColor: 'rgba(0,128,128,1)',
        borderWidth: 2,
        data: myData.map((item)=>{
          return item.EUR;
        })
      },
    //UU
      {
        label: 'UU',
        fill: true,
        lineTension: 0.5,
        backgroundColor: 'rgba(0,250,154,1)',
        borderColor: 'rgba(0,250,154,1)',
        borderWidth: 2,
        data: myData.map((item)=>{
          return item.UU;
        })
      },
    //LEI
      {
        label: 'LEI',
        fill:true,
        lineTension: 0.5,
        backgroundColor: 'rgba(0,255,0,1)',
        borderColor: 'rgba(0,255,0,1)',
        borderWidth: 2,
        data: myData.map((item)=>{
          return item.LEI;
        })
      },
    //UM
      {
        label: 'UM',
        fill: true,
        lineTension: 0.5,
        backgroundColor: 'rgba(255,215,0,1)',
        borderColor: 'rgba(255,215,0,1)',
        borderWidth: 2,
        data: myData.map((item)=>{
          return item.UM;
        })
      },
    //UT
      {
        label: 'UT',
        fill: true,
        lineTension: 0.5,
        backgroundColor: 'rgba(255,69,0,1)',
        borderColor: 'rgba(255,69,0,1)',
        borderWidth: 2,
        data: myData.map((item)=>{
          return item.UT;
        })
      },
    //UTi
      {
        label: 'UTi',
        fill:true,
        lineTension: 0.5,
        backgroundColor: 'rgba(240,128,128,1)',
        borderColor: 'rgba(240,128,128,1)',
        borderWidth: 2,
        data: myData.map((item)=>{
          return item.UTi;
        })
      },
      
    ]
}



//configurations
const config = {
      type: 'line',
      data : data,
      options: {
      //responsive: true,
        plugins: {
          title:{
            display:true,
            text:"PhD Database Visualization"
          },
          tooltip: {
            mode: 'index'
          }
        },
        interaction: {
          mode: 'nearest',
          axis: 'x',
          intersect: false
        },
        scales: {
          x: {
            title: {
              display: true,
              text: 'Years',
            }
          },
          y: {
            min:100,
            max:6000,
            stacked:true,
            title: {
              display: true,
              text: 'Count'
            }
          }
          
        }
      }
  };




function ThesesChart(){
  return(
    <div>
    <Line
    data={data}
    options={config.options}
    />
    </div>
  );
}

export default ThesesChart