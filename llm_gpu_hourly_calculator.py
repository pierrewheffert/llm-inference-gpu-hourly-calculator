#!/usr/bin/env python3
"""
LLM Inference GPU Hourly & Token Cost Calculator 2026.
Computes token throughput and cost per million tokens across popular open-weight models (Llama 3, Mistral, Qwen).
"""
import argparse

def calculate_llm_cost(tokens_per_second, gpu_hourly_rate, monthly_hours):
    tokens_per_hour = tokens_per_second * 3600.0
    monthly_tokens = tokens_per_hour * monthly_hours
    monthly_cost = gpu_hourly_rate * monthly_hours
    cost_per_million = (monthly_cost / monthly_tokens) * 1_000_000.0 if monthly_tokens > 0 else 0.0
    return {
        "tokens_per_hour": tokens_per_hour,
        "monthly_tokens": monthly_tokens,
        "monthly_cost": monthly_cost,
        "cost_per_million": cost_per_million
    }

def main():
    parser = argparse.ArgumentParser(description="LLM Inference GPU Hourly Cost Calculator")
    parser.add_argument("--tokens-per-sec", type=float, default=85.0, help="Throughput in tokens/sec (default: 85.0 on RTX 4090)")
    parser.add_argument("--rate", type=float, default=0.74, help="GPU hourly cost in USD (default: $0.74 for RTX 4090 Secure)")
    parser.add_argument("--hours", type=float, default=300.0, help="Active inference hours per month (default: 300)")
    args = parser.parse_args()

    res = calculate_llm_cost(args.tokens_per_sec, args.rate, args.hours)
    print(f"Monthly Output:          {res['monthly_tokens'] / 1e6:.2f}M tokens")
    print(f"Monthly Infrastructure:  ${res['monthly_cost']:.2f}")
    print(f"Cost Per Million Tokens: ${res['cost_per_million']:.4f}")

if __name__ == "__main__":
    main()
