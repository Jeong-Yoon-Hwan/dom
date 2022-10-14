import { ExchangeService, QuoationService } from 'node-upbit';
const quoationService = new QuoationService();
//마켓 코드 조회
const res = await quoationService.getMarketAllInfo();
// 분 캔들 조회
const res2 = await quoationService.getMinutesCandles({
  minutes: '60',
  marketCoin: 'KRW-BTC',
  count: 10,
});
// 일 캔들 조회
const res3 = await quoationService.getDayCandles({
  marketCoin: "KRW-BTC",
  count: 10,
});
// 현재가 정보 조회
const res4 = await quoationService.getTicker(['KRW-BTC']);
// 호가 정보 조회
const res5 = await quoationService.getOrderbook(['KRW-BTC']);
/*  인증키가 필요 */
const UBIT_ACCESS_KEY = "ATJIYyirxSDc3zW4cHkQVxem6mBMJw9WmiUvs1Uv";
const UBIT_SECRET_KEY = "xqGERO2vGc37lxhSIx5rEaNVidu09JfaPKsvx6Jp";
const exchangeService = new ExchangeService(UBIT_ACCESS_KEY, UBIT_SECRET_KEY);
//전체 계좌 조회
const res6 = await exchangeService.getAllAccount();
console.log(res6);
//주문 가능 정보
const res7 = await exchangeService.getOrderChance('KRW-BTC');
// API 키 리스트 조회
// const res8 = await exchangeService.getApiKeyStatus();