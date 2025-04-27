<template>
  <div :class="['app', weatherEffect]">
    <!-- 太陽 -->
    <div v-if="weatherEffect === 'sunny'" class="sun"></div>

    <!-- 雨滴容器 -->
    <div v-if="weatherEffect === 'rainy'" class="rain">
      <div v-for="n in 60" :key="n" class="raindrop" :style="{ left: `${Math.random() * 100}%`, animationDelay: `${Math.random() * 2}s` }"></div>
    </div>

    <!-- 卡片面板 -->
    <div class="card">
      <h1>情緒分析工具</h1>

      <textarea v-model="userInput" placeholder="請輸入文字..." rows="4"></textarea>
      <button @click="analyzeText">開始分析</button>

      <div class="result" v-if="result">
        <h2>分析結果：</h2>
        <p>{{ result }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      userInput: "",
      result: "",
      weatherEffect: "normal", // sunny, rainy, normal
    };
  },
  methods: {
    async analyzeText() {
      if (!this.userInput.trim()) return;

      try {
        const response = await axios.post("https://setitool-283670260072.asia-east1.run.app/analyze", {
          content: this.userInput,
        });
        //"http://localhost:8080/analyze"
        this.result = response.data.result || "回傳格式異常";

        if (this.result === "正面") {
          this.weatherEffect = "sunny";
        } else if (this.result === "負面") {
          this.weatherEffect = "rainy";
        } else {
          this.weatherEffect = "normal";
        }
      } catch (err) {
        this.result = "發生錯誤：" + err.message;
        this.weatherEffect = "normal";
      }
    },
  },
};
</script>

<style scoped>
/* 背景區域 */
.app {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  min-height: 100vh;
  transition: background 0.5s, color 0.5s;
  position: relative;
  overflow: hidden;
  font-family: 'Helvetica', 'Arial', sans-serif;
}

/* 卡片面板（主內容） */
.card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(6px);
  padding: 30px 24px;
  border-radius: 16px;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  width: 100%;
  z-index: 2;
  text-align: center;
  color: #333; /* 保持字體深色，無論背景 */
}

/* 情緒結果文字 */
.result {
  margin-top: 20px;
  font-size: 20px;
}

/* 控件樣式 */
textarea {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  border-radius: 8px;
  border: 1px solid #ccc;
  resize: vertical;
  margin-bottom: 15px;
  background: #fff;
}

button {
  padding: 10px 20px;
  background-color: #3b82f6;
  color: white;
  font-size: 16px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

button:hover {
  background-color: #2563eb;
}

/* 中立背景 - 淡淡的米白漸層 */
.app.normal {
  background: linear-gradient(to top left, #fdf6e3, #f5f5f5);
}

/* 晴天背景 - 藍粉漸層 */
.app.sunny {
  background: linear-gradient(to top right, #a1c4fd 0%, #c2e9fb 100%);
}

/* 雨天背景 - 深藍灰漸層 */
.app.rainy {
  background: linear-gradient(to top, #5d6d7e, #2c3e50);
}

/* 太陽動畫 */
.sun {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 70px;
  height: 70px;
  background: radial-gradient(circle, #ffec99, #fbc531);
  border-radius: 50%;
  animation: pulse 2s infinite;
  box-shadow: 0 0 20px 8px rgba(255, 215, 0, 0.6);
  z-index: 1;
}

@keyframes pulse {
  0% {
    transform: scale(1);
    opacity: 0.9;
  }
  50% {
    transform: scale(1.15);
    opacity: 1;
  }
  100% {
    transform: scale(1);
    opacity: 0.9;
  }
}

/* 雨滴效果 */
.rain {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
}

.raindrop {
  position: absolute;
  width: 2px;
  height: 18px;
  background: rgba(255, 255, 255, 0.7);
  border-radius: 1px;
  animation: drop 1.8s linear infinite;
}

@keyframes drop {
  0% {
    top: -20px;
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
  100% {
    top: 100%;
    opacity: 0;
  }
}
</style>